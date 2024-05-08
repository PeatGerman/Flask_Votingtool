import os
from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from app import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    auth = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)

    def get_id(self):
        return str(self.id)


class Voting(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voting_creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    start_date = db.Column(db.DateTime)
    enddate = db.Column(db.DateTime, nullable=True)
    acces_by_all = db.Column(db.Boolean)


class UserQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)
    voting_id = db.Column(db.Integer, db.ForeignKey('voting.id'), nullable=False)
    response_type = db.Column(db.Integer)
    global_use = db.Column(db.Boolean)


class PossibleSelectionOption(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_question_id = db.Column(db.Integer, db.ForeignKey('user_question.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)


class Tokenpool(db.Model):
    token = db.Column(db.String(255), primary_key=True)
    email = db.Column(db.String(255))
    voting_id = db.Column(db.Integer, db.ForeignKey('voting.id'))


class UserAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer_text = db.Column(db.String(255))
    user_question_id = db.Column(db.Integer, db.ForeignKey('user_question.id'), nullable=False)
    user_selected_option = db.Column(db.Integer, db.ForeignKey('possible_selection_option.id'))
    token = db.Column(db.String(255), db.ForeignKey('tokenpool.token'))
