import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        recon.adjust_for_ambient_noise(source, duration=3)  # Ajustando audio para melhorar o reconhecimento

        print('Say something: ')
        audio = recon.listen(source)

        print(recon.recognize_sphinx(audio))
