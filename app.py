from flask import Flask
import json



app = Flask(__name__)
app.secret_key =' '

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
