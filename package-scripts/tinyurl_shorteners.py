import pyshorteners

url = 'https://devguide.python.org/#status-of-python-branches'

short = pyshorteners.Shortener()
short_url = short.tinyurl.short(url)
print(short_url)
