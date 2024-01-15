from models import db, Hero, Power, HeroPower
from random import choice, randint
from app import app
from sqlalchemy import MetaData

def seed_data():
    with app.app_context():
        # Clear the database
        print("🗑️ Clearing the database...")
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print(f'Clear table {table}')
            db.session.execute(table.delete())
        db.session.commit()
        
        # Seeding powers
        print("🦸‍♀️ Seeding powers...")
        powers = [
            { "name": "super strength", "description": "gives the wielder super-human strengths" },
            { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
            { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
            { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
        ]
        for power in powers:
            p = Power(name=power['name'], description=power['description'])
            db.session.add(p)
        db.session.commit()

        # Seeding heroes
        print("🦸‍♀️ Seeding heroes...")
        heroes = [
            { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
            { "name": "Doreen Green", "super_name": "Squirrel Girl" },
            { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
            { "name": "Janet Van Dyne", "super_name": "The Wasp" },
            { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
            { "name": "Carol Danvers", "super_name": "Captain Marvel" },
            { "name": "Jean Grey", "super_name": "Dark Phoenix" },
            { "name": "Ororo Munroe", "super_name": "Storm" },
            { "name": "Kitty Pryde", "super_name": "Shadowcat" },
            { "name": "Elektra Natchios", "super_name": "Elektra" }
        ]
        for hero in heroes:
            h = Hero(name=hero['name'], super_name=hero['super_name'])
            db.session.add(h)
        db.session.commit()

        # Adding powers to heroes
        print("🦸‍♀️ Adding powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        all_heroes = Hero.query.all()
        all_powers = Power.query.all()
        for hero in all_heroes:
            for _ in range(randint(1, 3)):
                power = choice(all_powers)
                strength = choice(strengths)
                hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=strength)
                db.session.add(hero_power)
        db.session.commit()

        print("🦸‍♀️ Done seeding!")


if __name__ == "__main__":
    seed_data()

