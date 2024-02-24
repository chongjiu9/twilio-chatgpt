from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import askgpt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

# Fake database that stores user contact information
Users_db = {}

welcome_msg="Hello there! I'm Linda, your personalized AI assistant. What's your name?"


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    
    # Special prompt for new user
    user_info = request.form['From']
    if Users_db.get(user_info) is None:
        Users_db[user_info] = True
        r = MessagingResponse()
        r.message(welcome_msg)
        return str(r)
    
    chat_log = session.get('chat_log')
    answer, chat_log = askgpt(incoming_msg, chat_log)
    session['chat_log'] = chat_log
    

    r = MessagingResponse()
    r.message(answer)
    return str(r)