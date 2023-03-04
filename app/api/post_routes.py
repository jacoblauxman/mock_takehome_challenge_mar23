from flask import Blueprint, jsonify, request
from app.models import db, Post, Coffee
from app.forms import PostForm
from app.api.auth_routes import validation_errors_to_error_messages


post_routes = Blueprint('post', __name__)


@post_routes.route("/ping")
def get_post_ping():
    return {'status': 'good'}

@post_routes.route("/")
def get_all_posts():
    posts = Post.query.order_by(Post.created_at.asc()).all()
    res = [p.to_dict_w_coffee() for p in posts]

    return {"posts": res}

@post_routes.route("/<int:id>")
def get_one_post(id):
    post = Post.query.get(id)

    if post is None:
        return {"errors": ["NOT FOUND: Requested Post was Not Found"], "status": 404}

    return {"post": post.to_dict_w_coffee()}


@post_routes.route("/", methods=["POST"])
def add_post():
    form = PostForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_post = Post(
            title=form.data['title'],
            text=form.data['text'],
            rating=form.data['rating'],
            coffee_id=form.data['coffee']
        )

        db.session.add(new_post)
        db.session.commit()

        return {'post': new_post.to_dict()}

    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 400

@post_routes.route("/<int:id>", methods=["DELETE"])
def delete_one_post(id):
    post = Post.query.get(id)

    if post is None:
        return {"errors": ["NOT FOUND: Requested Post was Not Found"], "status": 404}

    else:
      db.session.delete(post)
      db.session.commit()
      return {"message": "Successfully Deleted Post. Good Bye, Brain Stew!"}


## Bonus Search Route ##

@post_routes.route("/coffee")
def get_posts_by_coffee():
    args = request.args
    posts = None
    if 'id' in args:
        posts = Post.query.filter(Post.coffee_id==args['id']).order_by(Post.created_at.asc()).all()

    else:
        posts = Post.query.where(Post.coffee.has(Coffee.name == args['name'])).order_by(Post.created_at.asc()).all()

    if len(posts)==0:
        return {'posts': [], 'message': ["No Results Found! Refine your search and try again!"]}

    else:
        return {'posts': [p.to_dict_w_coffee() for p in posts]}
