from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

with open(r'barcode.png', 'wb') as f:
    EAN13('012345678913', writer=ImageWriter()).write(f)

    img = Image.open('barcode.png')
    img.show()
