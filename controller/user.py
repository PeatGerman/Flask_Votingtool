from flask import Blueprint, render_template, request, redirect, url_for
import requests
from flask_login import login_required

user = Blueprint('user', __name__)


@login_required
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
    from datetime import datetime
    data = request.form
    print(data)
    from app import db
    from db.models import Voting, UserQuestion, PossibleSelectionOption
    # Erstellung eines neuen Voting-Eintrags
    new_voting = Voting(
        voting_creator_id=1,  # Angenommen, der Benutzer mit ID 1 erstellt die Umfrage
        start_date=datetime.strptime(data['calendar_day'], '%d/%m/%Y'),
        acces_by_all=True  # Hier anpassen, je nach Bedarf
    )
    db.session.add(new_voting)
    db.session.flush()  # ID von new_voting wird benötigt für die Fragen

    # Durchgehen der Fragen und Antworten
    questions = {key: value for key, value in data.items() if key.startswith('questions')}
    for q_key, q_text in questions.items():
        # Extrahieren der Frage-Nummer
        q_number = q_key.split('[')[-1].rstrip(']')
        response_type = data.get(f'answerType{q_number}')
        # Neuen Frage-Eintrag erstellen
        new_question = UserQuestion(
            text=q_text,
            voting_id=new_voting.id,
            response_type=response_type,
            global_use=False  # Beispielweise immer False, anpassen je nach Bedarf
        )
        db.session.add(new_question)
        db.session.flush()  # ID von new_question wird benötigt für die Antwortoptionen

        # Antwortoptionen für diese Frage
        options = data.getlist(f'answers{q_number}[]')
        for option_text in options:
            new_option = PossibleSelectionOption(
                user_question_id=new_question.id,
                text=option_text
            )
            db.session.add(new_option)

    db.session.commit()

    return f"Voting ID {new_voting.id} gespeichert mit {len(questions)} Fragen."

    #  print(request.form)
    #  for key, values in request.form.lists():
    #      print(f"headline: {key}")
    #      for value in values:
    #          print(f"Value: {value}")
    #          print(" ")
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
