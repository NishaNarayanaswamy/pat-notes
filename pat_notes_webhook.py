import logging
from flask import Flask
from flask_assistant import Assistant, ask, tell, context_manager

app = Flask(__name__)
assist = Assistant(app)
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)


@assist.action('capture_msg')
def greet_and_start():
    speech = "Hey! You said blah."
    return ask(speech)

if __name__ == '__main__':
    app.run(debug=True)
