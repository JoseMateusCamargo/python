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
