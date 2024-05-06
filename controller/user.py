from flask import Blueprint, render_template, request, redirect, url_for
import requests

user = Blueprint('user', __name__)


@user.route('/generate_voting', methods=['GET', 'POST'])
def login_page():
    return render_template("generate_voting.html")


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
    print(request.form)
    for key, values in request.form.lists():
        print(f"headline: {key}")
        for value in values:
            print(f"Value: {value}")
            print(" ")
    return redirect(url_for('user.login_page'))


@user.route('/test_survey', methods=['GET', 'POST'])
def voting_overview():

    return render_template("voting_overview.html")


######################################################################       Test stuff

def response_index():
    return redirect(url_for('user.index'))


@user.route('/test_answer', methods=['GET', 'POST'])
def generate_response():
    url = 'http://localhost:5000/user/submit_survey'
    testnumber = 2
    data = {'testnumber': testnumber}
    match testnumber:
        case 1:
            data = {
                'surveyTitle': 'Überschrift',
                'calendar_day': '02/04/2024',
                'questions[1]': 'Frage',
                'answerType1': 'single_choice',
                'answers1[]': ['Antwortmöglichkeit1', 'Antwortmöglichkeit2']
            }
        case 2:
            data = {
                'surveyTitle': 'Überschrift_1',
                'calendar_day': '02/04/2024',
                'questions[1]': 'Frage_1',
                'answerType1': 'single_choice',
                'answers1[]': ['Antwortmöglichkeit1_1', 'Antwortmöglichkeit2_1'],
                'questions[2]': 'Frage_2',
                'answerType2': 'multiple_choice',
                'answers2[]': ['Antwortmöglichkeit1_2', 'Antwortmöglichkeit2_2'],
                'questions[3]': 'Frage_3',
                'answerType3': 'free_text',
                'answers3[]': ['Antwortmöglichkeit1_3', 'Antwortmöglichkeit2_3'],
                'questions[5]': 'Skala',
                'answerType5': 'scale_rating',
                'answers5[]': '3'
            }

    response = requests.post(url, data=data)
    return response_index()


@user.route('/')
def index():
    return render_template('index.html')
