import logging
from flask import Flask
from flask_assistant import Assistant, ask, tell, context_manager

app = Flask(__name__)
assist = Assistant(app)
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)


@assist.action('greeting')
def greet_and_start():
    speech = "Hey! Are you male or female?"
    return ask(speech)


@assist.action("user-gender")
def ask_for_color():    
    speech = 'Hi there! What is your favorite color?'
    return ask(speech)


@assist.action('give-color')
def repeat_color():
    speech = 'Color'
    return ask(speech)


if __name__ == '__main__':
    app.run(debug=True)
