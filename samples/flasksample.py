from flask import Flask
app = Flask(__name__)


@app.route('/')
def hallo_welt():
    return 'Hallo, Welt!'

# app.run(debug=True, use_debugger=True, use_reloader=True, port=5000)

# $ FLASK_APP=flasksample.py flask run --reload