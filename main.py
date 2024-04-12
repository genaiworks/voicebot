import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pygame import mixer
from io import BytesIO
import os
import openai

openai.api_key="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"

message_array = [{'role': 'system', 'content': 'You are my boyfriend names Ali'}]

#capture voice
def listen():
    r = sr.Recognizer()
    #get audio
    with sr.Microphone() as source:
        print(' Listening ')
        r.pause_threshold =1
        audio =  r.listen(source)
    
    try:
        #transcribe audio
        print('Recognizing... ')
        query = r.recognize_google(audio, language ='en-in')
        print(f'user has said {query}')
        message_array.append({'role': 'user', 'content': query})
        respond(audio)
    except Exception as e:
        print(e)
        print('Say that again please')

#respond to the conversation
def respond(audio):
    print('Responding ...')
    #use gpt to response to messages array
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=message_array
    )
    res_message = response.choices[0].message
    message_array.append(res_message)
    speak(res_message.content)

#speak out the audio response
def speak(text):
    speech = gTTS(text=text, lang='en', slow=False)
    speech.save('captured_voice.mp3')
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')
    listen()

query = listen()






