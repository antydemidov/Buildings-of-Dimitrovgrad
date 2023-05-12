from ast import Pass

from django.shortcuts import render
from flask_login import user_accessed
from flask_wtf import FlaskForm
from wtforms import (PasswordField, RadioField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired("Поле необходимо заполнить!")])
    password1 = PasswordField('Password', validators=[DataRequired(
        "Поле необходимо заполнить!"), Length(6, 10, 'Пароль должен содержать от 6 до 10 символов!')])
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired("Поле необходимо заполнить!")])
    password1 = PasswordField('Password', validators=[DataRequired(
        "Поле необходимо заполнить!"), Length(6, 10, 'Пароль должен содержать от 6 до 10 символов!')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired("Поле необходимо заполнить!"), EqualTo(
        'password1', "Пароли не совпадают!"), Length(6, 10, 'Пароль должен содержать от 6 до 10 символов!')])
    submit = SubmitField('Sign Up')


class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired(
        "Поле необходимо заполнить!")], default='Search', render_kw={'class': 'btn btn-success btn-block'})
    submit = SubmitField('Search', render_kw={
                         'class': 'btn btn-success btn-block'})


class FilterForm(FlaskForm):
    field = SelectField('Select', choices=[
                        '---', 'Actual', 'Not actual'], render_kw={'class': 'btn btn-success btn-block'})
    submit = SubmitField('Select', render_kw={
                         'class': 'btn btn-success btn-block'})


class LengthSelector(FlaskForm):
    selector = SelectField('Select', choices=[12, 24, 48, 96], render_kw={
                           'class': 'btn btn-success btn-block'})
