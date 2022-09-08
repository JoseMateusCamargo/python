from gtts import gTTS
from pygame import mixer
import os

voice = gTTS("Synthesis with GTTS (Google-text-to-Speech)")
voice.save('synthesis_en.mp3')

voice_pt = gTTS("Sintetização com GTTS", lang='pt')
voice_pt.save('assets/synthesis_pt.mp3')

# -------------------- [1] Method: Using OS to open .mp3.
os.system('synthesis_en.mp3')

# -------------------- [2] Method: Using pygame to open .mp3.
mixer.init()
mixer.music.load('assets/synthesis_pt.mp3')
mixer.music.play()

x = input('Click to stop...')
