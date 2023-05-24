from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('start output.mp3')

user_input = input("Enter the text to convert to speech: ")
text_to_speech(user_input)
