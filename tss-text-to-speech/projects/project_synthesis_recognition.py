import os
import pyttsx3
import speech_recognition as sr


def set_property():
    en.setProperty('voice', b'english')
    en.setProperty('rate', 140)
    en.setProperty('volume', 1)
    en.runAndWait()


en = pyttsx3.init()
en.say('Hello boss, would you like to listen one music? yes or no')
set_property()
recon = sr.Recognizer()

with sr.Microphone() as source:
    audio_data = recon.listen(source)
    resp = recon.recognize_google(audio_data, language='en')
    print(resp)

if resp == 'yes':
    en.say('OK, opening music...')
    set_property()
    os.system('assets/audio.wav')

elif resp == 'no':
    en.say('OK, closing application...')
    set_property()
