from gtts import gTTS
from pygame import mixer
import os.path

file_path = input("Type file path: ")

if os.path.isfile(file_path):
    print("Loading...")
    file_data = open(file_path)
    file_data = file_data.read()

    print("Saving...")
    voice = gTTS(file_data, lang='en')
    voice.save("assets/read_file.mp3")

    print("Speaking...")
    mixer.init()
    mixer.music.load('assets/read_file.mp3')
    mixer.music.play()

    x = input('Click to stop...')

else:
    print("File not exists")
