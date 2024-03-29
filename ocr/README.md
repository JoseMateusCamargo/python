<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python

## Optical Character Recognition (OCR)

Dentro da área da Visão Computacional existe a sub-área de Reconhecimento Ótico de Caracteres (ou OCR – Optical
Character Recognition) que basicamente visa transformar imagens em textos. Em outras palavras, o OCR pode ser descrito
como a conversão de imagens contendo texto digitado, escrito a mão ou impresso, em caracteres que uma máquina é capaz
de entender.

#### _Let's Code!_

- Reconhecer e “ler” o texto com usando `Google's Tesseract-OCR`.
- Detecção de texto de imagens usando `EasyOCR`.

---

**Detecção de texto de imagens usando `EasyOCR`**

```python
import easyocr

reader = easyocr.Reader(['pt'])
img = '../../assets/img/img_to_read.jpg'

result = reader.readtext(img, paragraph=False)

for results in result:
    print(f'Text:\n'
          f'\tPosition: {results[0]}\n'
          f'\tText: {results[1]}\n')

```

**Reconhecer e “ler” o texto com usando `Google's Tesseract-OCR`**

```python
# pip install pytesseract
# pip install Pillow
# pip install pywhatkit

import os
from PIL import Image  # Importing Pillow module to open image in script
import pytesseract  # Module to using OCR technology
import pywhatkit as kit

# Documentation: https://pypi.org/project/pytesseract/
# Set the Path of Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:/Users/.../AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

# Change the directory to the location where image is present
os.chdir(r"../../assets/img")

# Load the Image
img = Image.open('Sem Título.png')

# Convert Image to Text
text = pytesseract.image_to_string(img)
print(text)

# To save Text using pywhatkit
kit.text_to_handwriting(text, "handwriting.png", (18, 10, 143))
```