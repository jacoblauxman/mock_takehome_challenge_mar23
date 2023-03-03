from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Coffee

coffee_routes = Blueprint('coffee', __name__)

@coffee_routes.route("/ping")
def get_coffee_ping():
    return {'status':'good'}


@coffee_routes.route("/")
def get_all_coffees():
    coffees = Coffee.query.order_by(Coffee.name.asc()).all()
    res = [c.to_dict() for c in coffees]

    return {'coffees': res}

@coffee_routes.route("/<int:id>")
def get_one_coffee(id):
    coffee = Coffee.query.get(id)

    if coffee is None:
        return {"errors": ["NOT FOUND: Requested Coffee was Not Found"], "status": 404}

    return {"coffee": coffee.to_dict()}


@coffee_routes.route("/delete/<int:id>")
def delete_one_coffee(id):
    coffee = Coffee.query.get(id)

    if coffee is None:
        return {"errors": ["NOT FOUND: Requested Coffee was Not Found"], "status": 404}

    else:
      db.session.delete(coffee)
      db.session.commit()
      return {"message": "Successfully Deleted Coffee. Good Bye, Bean Juice!"}
