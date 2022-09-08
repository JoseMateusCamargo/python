import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile("../assets/audio.wav") as font:
    audio = r.record(font)

try:
    # Utiliza chave de API padrão, consultar documentação para utilizar chave particular.
    # Documentation: https://cloud.google.com/speech-to-text
    text = r.recognize_google(audio, language='pt-br')
    print(f'Google speech recognition understood: \n{text}')

except sr.UnknownValueError:
    print('Google speech recognition could not understand audio!')

except sr.RequestError as e:
    print(f'Google speech recognition API Error: {str(e)}')
