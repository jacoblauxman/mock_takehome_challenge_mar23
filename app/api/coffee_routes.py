from flask import Blueprint, jsonify, request
from app.models import db, Coffee
from app.forms import CoffeeForm
from app.api.auth_routes import validation_errors_to_error_messages


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


@coffee_routes.route("/create", methods=["POST"])
def add_coffee():
    form = CoffeeForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_coffee = Coffee(
            name=form.data['name'],
            year=form.data['year'],
            caffeine_content=form.data['caffeine_content']
          )
        db.session.add(new_coffee)
        db.session.commit()

        return {'coffee': new_coffee.to_dict()}

    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 400





@coffee_routes.route("/delete/<int:id>")
def delete_one_coffee(id):
    coffee = Coffee.query.get(id)

    if coffee is None:
        return {"errors": ["NOT FOUND: Requested Coffee was Not Found"], "status": 404}

    else:
      db.session.delete(coffee)
      db.session.commit()
      return {"message": "Successfully Deleted Coffee. Good Bye, Bean Juice!"}
