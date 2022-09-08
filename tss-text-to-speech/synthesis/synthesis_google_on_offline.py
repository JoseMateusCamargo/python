from playsound import playsound
import gtts  # To online Mode
import pyttsx3  # To offline Mode

TEXT = 'Hello everybody'

# -------------------- [1] Method: Online Mode.
tts = gtts.gTTS(TEXT, lang='pt-br')
tts.save('assets/audio.mp3')
playsound('assets/audio.mp3')

# -------------------- [2] Method: Offline Mode.
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(voice.name)

engine.setProperty('voice', 'brazil')
engine.say(TEXT)
engine.runAndWait()
