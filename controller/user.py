from flask import Blueprint, render_template, request, redirect, url_for

user = Blueprint('user', __name__)


@user.route('/generate_voting', methods=['GET', 'POST'])
def login_page():
    return render_template("create_voting.html")


@user.route('/vote', methods=['POST'])
def vote():
    # code for handling the vote
    pass


@user.route('/results')
def results():
    # code for displaying the voting results
    pass


@user.route('/submit_survey', methods=['GET', 'POST'])
def insert_vote():

    #print(request.form)
    for key, values in request.form.lists():
        print(f"headline: {key}")
        for value in values:
            print(f"Value: {value}")
    print(" ")
    return redirect(url_for('user.login_page'))
