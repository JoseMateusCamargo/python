import pyttsx3
from datetime import datetime

now = datetime.now()
name = "Chefe"
hour = now.hour
minute = now.minute

text = "Ola " + str(name) + ", seja bem vindo, hora atual: " + str(hour) + " horas e " + str(minute) + " minutos."

engine = pyttsx3.init()

engine.setProperty('voice', b'brazil')
engine.setProperty("rate", 190)  # Speed
engine.setProperty("volume", 1)  # Volume
engine.say(text)
engine.runAndWait()
