# Install wkhtmltopdf, documentation: https://wkhtmltopdf.org/

import pdfkit  # Documentation: https://github.com/JazzCore/python-pdfkit

# Simple use
pdfkit.from_url('http://google.com', 'out.pdf')
pdfkit.from_file('test.html', 'out.pdf')
pdfkit.from_string('Hello!', 'out.pdf')

# You can pass a list with multiple URLs or files
pdfkit.from_url(['google.com', 'yandex.ru', 'engadget.com'], 'out.pdf')
pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')

# Using wkhtmltopdf options
options = {
    'page_size': 'A4',
    'margin-top': '0.5in',
    'margin-right': '0.5in',
    'margin-bottom': '0.5in',
    'margin-left': '0.5in',
    'encoding': 'UTF-8'
}

pdfkit.from_file(input='test.html', output_path='out.pdf', css='test.css', options=options)

# Also you can pass an opened file
with open('file.html') as f:
    pdfkit.from_file(f, 'out.pdf')
