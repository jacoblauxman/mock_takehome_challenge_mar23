from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length, Regexp, ValidationError


class CoffeeForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    year = IntegerField('year', validators=[DataRequired()])
    caffeine_content = FloatField('caffeine content', validators=[DataRequired()])
    submit = SubmitField('submit')
