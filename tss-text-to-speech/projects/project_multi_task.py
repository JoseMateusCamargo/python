import pyttsx3
import speech_recognition as sr
import webbrowser


def set_property():
    en.setProperty('voice', b'english')
    en.setProperty('rate', 140)
    en.setProperty('volume', 1)
    en.runAndWait()


en = pyttsx3.init()
print('Hello boss, would you like to open a website?')
set_property()
recon = sr.Recognizer()

with sr.Microphone() as source:
    audio_data = recon.listen(source)
    resp = recon.recognize_google(audio_data, language='en')
    print(resp)

if resp == 'Open Google':
    en.say('OK, opening Google.')
    set_property()
    webbrowser.open('www.google.com')

elif resp == 'Open Youtube':
    en.say('OK, opening Youtube Site.')
    set_property()
    webbrowser.open('www.youtube.com')

else:
    en.say('Sorry, something went wrong... I not understand the command.')
    set_property()
