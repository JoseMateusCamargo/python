import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print('Description the multiplication: ')  # Example: 9 x 5
        audio = recon.listen(source)

        txt_sum = recon.recognize_google(audio, language='pt')

        if txt_sum == 'close':
            break

        print(f'Multiplication: {str(txt_sum)}')
        print(f'Result: {str(int(txt_sum[0]) * int(txt_sum[4]))}')
        # txt_sum[0] = 9 of [9 x 5]
        # txt_sum[4] = 5 of [9 x 5]
