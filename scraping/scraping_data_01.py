import requests
from bs4 import BeautifulSoup

# Searching
url = requests.get('https://fundamentus.com.br/fii_resultado.php', headers={'User-Agent': 'Mozilla/5.0'})

# Instance
soup = BeautifulSoup(url.text, 'html.parser')

# Find element
data = soup.find("table", {"id": "tabelaResultado"}).find("tbody").find_all("tr")

for base in data:
    base_ = base.find_all("td")
    print(
        f"[{base_[0].text}]\n"
        f"\tSeguimento: {base_[1].text}\n"
        f"\tCotacao: {base_[2].text}\n"
        f"\tValor de Mercado: {base_[6].text}\n"
    )
