from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField, IntegerField
from wtforms.validators import DataRequired
from database.models import *

class add_game(FlaskForm):
    game_name = StringField('Game Name', validators=[DataRequired('Обязательно')])
    game_description = StringField('Game Description', validators=[DataRequired('Обязательно')])
    quantity = IntegerField('Game Quantity', validators=[DataRequired('Обязательно')])
    game_prices = FloatField('Game Price', validators=[DataRequired('Обязательно')])
    game_link = StringField('Game Link', validators=[DataRequired('Обязательно')])
    add = SubmitField('Добавить игру')

class login(FlaskForm):
    email =StringField('Введите почту', validators=[DataRequired()])
    password = StringField('Введите пароль', validators=[DataRequired()])
    login = SubmitField('Войти/Зарегистрироваться')

class delete_game(FlaskForm):
    id = IntegerField('Введите id игры', validators=[DataRequired('Обязательно')])
    delete = SubmitField('Удалить')


