from flask import Flask
import json



app = Flask(__name__)

file_path = "config/secret_key.json"
with open(file_path, 'r') as file:
    config_secret_key = json.load(file)

app.secret_key = config_secret_key['secret_key']

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
