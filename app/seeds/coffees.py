from app.models import db, Coffee, environment, SCHEMA
import random

def seed_coffees():
    names = ['Black', 'Cappucino', 'Java', 'Breakfast Blend', 'Latte', 'Americano', 'Red Eye', 'Black Eye']
    years = [2000, 2001, 2023, 2006, 2011, 2020, 2015, 1999, 1878, 1995, 2022]

    for i in range(20):
        new_coffee = Coffee(
            name=random.choice(names),
            year=random.choice(years)
        )

        db.session.add(new_coffee)
        db.session.commit()


def undo_coffees():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.coffees RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM coffees")

    db.session.commit()
