import sqlalchemy
from db.models import *


def get_user_by_email(email):
    user = Users.query.filter_by(email=email).first()
    print("user_helpers:" + str(user))
    return user


def create_user(email, password):
    user = Users(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def load_users(email):
    user = Users.query.filter_by(email=email).first()
    if user:
        return user.id
    return None
