import speech_recognition as sr  # pip install SpeechRecognition
import os

print('Hello boss, would you like to open the Chrome?')
recon = sr.Recognizer()

with sr.Microphone() as source:
    audio_data = recon.listen(source)
    resp = recon.recognize_google(audio_data, language='en')

if resp == 'yes':
    print('Ok, opening chrome...')
    open_ = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    os.system(open_)

elif resp == 'no':
    print('Lol, no problem...')
