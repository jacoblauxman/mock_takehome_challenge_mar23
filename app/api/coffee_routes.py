from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

coffee_routes = Blueprint('coffee', __name__)
