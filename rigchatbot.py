import pygame
import os
from gtts import gTTS

def chatbot_response(user_input):
    user_input=user_input.lower()

    if 'hello' in user_input or 'hi' in user_input or 'hey there' in user_input:
        response="Hello! How can I help you today?"
    elif 'how are you' in user_input or 'how have you been' in user_input:
        response="I'm just a computer program, but I'm here to help you!"
    elif 'your name' in user_input or (('who' in user_input) and ('you' in user_input)) or (('what' in user_input) and ('call you' in user_input)):
        response="I am your friendly chatbot. I don't have a specific name."
    elif 'bye' in user_input or 'see you later' in user_input or 'farewell' in user_input:
        response="Goodbye! Have a great day!"
    elif 'where' in user_input and 'you' in user_input:
        response='I am in your computer.'
    elif 'what' in user_input and 'your' in user_input and 'capabilities' in user_input:
        response='I can respond to basic greetings like "hello", "how are you?".'
    else:
        response="I'm not sure how to respond to that. Can you please ask something else?"
    return response

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    c=1
    while(c==1):
        user_input=input("You: ")
        if 'bye' in user_input.lower():
            c=0
        response = chatbot_response(user_input)
        print("Bot:", response)
        obj=gTTS(text=response,lang='en',slow='False')
        obj.save('respond.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load("respond.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(100)
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        os.remove("respond.mp3")

chat()
