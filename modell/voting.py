from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    auth = db.Column(db.Integer)


class Voting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voting_creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    enddate = db.Column(db.DateTime)
    acces_by_all = db.Column(db.Boolean)


class UserQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    voting_id = db.Column(db.Integer, db.ForeignKey('voting.id'), nullable=False)
    response_type = db.Column(db.Integer)
    global_use = db.Column(db.Boolean)


class PossibleSelectionOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_question_id = db.Column(db.Integer, db.ForeignKey('user_question.id'), nullable=False)
    text = db.Column(db.String, nullable=False)


class UserAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String)
    user_question_id = db.Column(db.Integer, db.ForeignKey('user_question.id'), nullable=False)
    user_selected_option = db.Column(db.Integer, db.ForeignKey('possible_selection_option.id'))
    token = db.Column(db.String, db.ForeignKey('tokenpool.token'))


class Tokenpool(db.Model):
    token = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)
    voting_id = db.Column(db.Integer, db.ForeignKey('voting.id'))
