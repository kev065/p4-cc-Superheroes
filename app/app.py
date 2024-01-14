from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ('''<h1> Superheroes API</h1>
                <h2>Welcome to the Superheroes API!</h2>''')

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_dict = [
        {"id": hero.id, "name": hero.name, "super_name": hero.super_name}
        for hero in heroes
    ]
    return make_response(jsonify(hero_dict), 200)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero is None:
        return make_response(jsonify({"error": "Hero not found"}), 404)
    powers_dict = [
        {"id": hero_power.power.id, "name": hero_power.power.name, "description": hero_power.power.description}
        for hero_power in hero.powers
    ]
    hero_dict = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": powers_dict
    }
    return make_response(jsonify(hero_dict), 200)


@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_dict = [
        {"id": power.id, "name": power.name, "description": power.description}
        for power in powers
    ]
    return make_response(jsonify(powers_dict), 200)

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
    power_dict = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }
    return make_response(jsonify(power_dict), 200)

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
        powers_dict = [
            {"id": power.id, "name": power.name, "description": power.description}
            for power in hero.powers
        ]
        hero_dict = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": powers_dict
        }
        return make_response(jsonify(hero_dict), 200)
    else:
        return make_response(jsonify({"errors": ["validation errors"]}), 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
