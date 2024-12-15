#!/usr/bin/env python3

from flask import Flask, render_template
from agents import ClothingAssistant, ActivityAssistant, MealAssistant, UserProxy

app = Flask(__name__)

def get_conversation():
    clothing_assistant = ClothingAssistant()
    activity_assistant = ActivityAssistant()
    meal_assistant = MealAssistant()
    user_proxy = UserProxy()

    conversation = []

    def log_conversation(agent, message):
        conversation.append({'agent': agent, 'text': message})

    
    log_conversation('User', "What should I wear today?")
    log_conversation('Clothing Assistant', user_proxy.initiate_chat(clothing_assistant, message="What should I wear today?").chat_history[3]['content'])

    
    log_conversation('User', "What should I do today?")
    log_conversation('Activity Assistant', user_proxy.initiate_chat(activity_assistant, message="What should I do today?").chat_history[3]['content'])

    
    log_conversation('User', "Where should I eat today?")
    log_conversation('Meal Assistant', user_proxy.initiate_chat(meal_assistant, message="Where should I eat today?").chat_history[3]['content'])

    return conversation

@app.route('/')
def index():
    conversation = get_conversation()
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)
