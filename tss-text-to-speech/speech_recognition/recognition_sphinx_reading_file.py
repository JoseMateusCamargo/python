import speech_recognition as sr

recon = sr.Recognizer()

PATH = '../assets/audio.wav'

with sr.AudioFile(PATH) as source:
    audio = recon.record(source)

print(recon.recognize_sphinx(audio))
