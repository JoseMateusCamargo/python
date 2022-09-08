import pyttsx3

engine = pyttsx3.init()

# Changing voices (id list)
voices = engine.getProperty('voices')

engine.setProperty("rate", 230)  # Speed 
engine.setProperty("volume", 1)  # Volume

# Printing voice's List
for voice in voices:
    engine.setProperty('voice', voice.id)
    print(voice)
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()

    if u'PT-BR' in voice.id:
        print('Wow, BR here...')
