from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

post_routes = Blueprint('post', __name__)
