from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    auth = db.Column(db.Integer, nullable=False)


class Voting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voting_creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    access_by_all = db.Column(db.Boolean, nullable=False)


class UserQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    voting_id = db.Column(db.Integer, db.ForeignKey('voting.id'), nullable=False)
    response_type = db.Column(db.Integer, nullable=False)
    global_use = db.Column(db.Boolean, nullable=False)


class PossibleSelectionOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_question_id = db.Column(db.Integer, db.ForeignKey('user_question.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)


class UserAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String(255))
    user_question_id = db.Column(db.Integer, db.ForeignKey('user_question.id'), nullable=False)
    user_selected_option = db.Column(db.Integer, db.ForeignKey('possible_selection_option.id'))
    token = db.Column(db.String(255))


class TokenPool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    voting_id = db.Column(db.Integer, db.ForeignKey('voting.id'), nullable=False)
