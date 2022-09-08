# Documentation: https://docs.python.org/3/library/zipfile.html

from zipfile import ZipFile

file = '../assets/zipfile.zip'

with ZipFile(file, 'r') as zip:
    zip.printdir()

    # ZipFile.extractall(path=None, members=None, pwd=None)
    zip.extractall('extractall')
    print('Unzipped in extractall folder')
