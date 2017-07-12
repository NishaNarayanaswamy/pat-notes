import logging
from flask import Flask
from flask_assistant import Assistant, ask, tell, context_manager

app = Flask(__name__)
assist = Assistant(app)
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

session_filename = 'user_sess.txt'
file = open(session_filename, 'a')

@assist.action('capture')  # specify intent name
def capture_note(note):
    file.write(str(note))
    speech = "you said... "+note+' \nAnything else to add?'
    return ask(speech)

@assist.action('appendNote')  # specify intent name
def capture_note(appendNote):
    file.write(str(appendNote))
    speech = "added note... "+appendNote
    return ask(speech)

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
