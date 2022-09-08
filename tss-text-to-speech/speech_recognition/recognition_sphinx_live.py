from pocketsphinx import LiveSpeech

for phrase in LiveSpeech:
    print(f'Você disse: {str(phrase)}')
