from flask import Blueprint, render_template, request, redirect, url_for, session, g, jsonify
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from modell.user_helpers import get_user_by_email



auth = Blueprint('/', __name__)




@auth.route('/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        # session.pop('username', None)
        usermail = request.form['email']
        password = request.form['password']

        # Überprüfe, ob der Benutzername in der Datenbank vorhanden ist
        user = get_user_by_email(usermail)
        if user is not None:
            # Überprüfe das Passwort
            if check_password_hash(user.password, password):
                # Logge den Benutzer ein, wenn das Passwort korrekt ist
                login_user(user)

                return redirect(url_for('user.index'))
            else:
                print("wrong email or password")
                # Falsches Passwort oder E-Mail
                return render_template('login.html', error='Ungültige Anmeldeinformationen')
        else:
            print("wrong email or password")
            # Falsches Passwort oder E-Mail
            return render_template('login.html', error='Ungültige Anmeldeinformationen')
    else:
        # Besucherseite ohne eingeloggt zu sein
        return render_template('login.html')


@auth.route('/logout')
def logout_page():
    logout_user()
    return 'Sie sind jetzt abgemeldet!'

@auth.route('/Sign-up')
def signup_page():
    return 0


@auth.route('/session-data')
def session_data():
    # Extrahieren aller relevanten Sitzungsdaten
    session_info = {
        'user_id': session.get('_user_id'),
        'fresh': session.get('_fresh'),
        'session_id': session.get('_id'),
        'remember': session.get('_remember'),
        'remember_seconds': session.get('_remember_seconds', 'Nicht gesetzt')
    }
    return jsonify(session_info)