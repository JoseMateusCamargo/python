import easyocr

reader = easyocr.Reader(['pt'])
img = '../../assets/img/img_to_read.jpg'

result = reader.readtext(img, paragraph=False)

for results in result:
    print(f'Text:\n'
          f'\tPosition: {results[0]}\n'
          f'\tText: {results[1]}\n')
