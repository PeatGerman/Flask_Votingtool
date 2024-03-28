from flask import Blueprint, render_template

auth = Blueprint('/', __name__)

@auth.route('/login')
def login_page():
    return render_template("login.html")

@auth.route('/logout')
def logout_page():
    return 0

@auth.route('/Sign-up')
def signup_page():
    return 0