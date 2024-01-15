from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower, HeroSchema, PowerSchema, HeroPowerSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# Initializes marshmallow
from models import ma
ma.init_app(app)

# Create schema instances
hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)
power_schema = PowerSchema()
powers_schema = PowerSchema(many=True)

@app.route('/')
def home():
    return ('''<h1> Superheroes API</h1>
                <h2>Welcome to the Superheroes API!</h2>''')

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_schema = HeroSchema(many=True)
    return make_response(jsonify(hero_schema.dump(heroes)), 200)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero is None:
        return make_response(jsonify({"error": "Hero not found"}), 404)
    hero_schema = HeroSchema()
    return make_response(jsonify(hero_schema.dump(hero)), 200)

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    power_schema = PowerSchema(many=True)
    return make_response(jsonify(power_schema.dump(powers)), 200)

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def get_or_update_power(id):
    power = Power.query.get(id)
    if power is None:
        return make_response(jsonify({"error": "Power not found"}), 404)
    if request.method == 'PATCH':
        description = request.json.get('description')
        if description is not None and len(description) >= 20:
            power.description = description
            db.session.commit()
        else:
            return make_response(jsonify({"errors": ["validation errors"]}), 400)
    power_schema = PowerSchema()
    return make_response(jsonify(power_schema.dump(power)), 200)

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    strength = request.json.get('strength')
    power_id = request.json.get('power_id')
    hero_id = request.json.get('hero_id')
    if strength in ['Strong', 'Weak', 'Average']:
        hero_power = HeroPower(strength=strength, power_id=power_id, hero_id=hero_id)
        db.session.add(hero_power)
        db.session.commit()
        hero = Hero.query.get(hero_id)
        hero_schema = HeroSchema()
        return make_response(jsonify(hero_schema.dump(hero)), 200)
    else:
        return make_response(jsonify({"errors": ["validation errors"]}), 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
