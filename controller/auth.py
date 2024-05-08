from flask import Blueprint, render_template, request, redirect, url_for, session, g
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash
from modell.user_helpers import get_user_by_email



auth = Blueprint('/', __name__)




@auth.route('/', methods=['GET', 'POST'])
def login_page():

    if request.method == 'POST':
        #session.pop('username', None)
        usermail = request.form['email']
        password = request.form['password']

        #Überprüfe, ob der Benutzername in der Datenbank vorhanden ist
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
    return 0

@auth.route('/Sign-up')
def signup_page():
    return 0


