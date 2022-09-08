from bs4 import BeautifulSoup
import requests

url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/2187/louveira-sp"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

print('Summary: ' + soup.find(class_='-gray -line-height-24 _center').text)
print('Min Temp: ' + soup.find(id='min-temp-1').string)
print('Max Temp: ' + soup.find(id='max-temp-1').string)
