from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length, Regexp, ValidationError, InputRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import db, Coffee


def coffee_choices():
    coffees = Coffee.query.all()
    return [(c.id, c.name) for c in coffees]
    return Coffee.query

class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=5, max=255)])
    text = TextAreaField('text', validators=[DataRequired(), Length(min=20, max=2000)])
    rating = IntegerField('rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    coffee = QuerySelectField(query_factory=coffee_choices, get_label='name', validators=[InputRequired('Please Provide a Coffee Choice')])
    submit = SubmitField('submit')
