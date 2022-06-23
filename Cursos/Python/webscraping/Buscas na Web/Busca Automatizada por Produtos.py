# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup

print()

url_base = 'https://lista.mercadolivre.com.br/'

input_ = str(input('Digite o nome do produto: '))

response = requests.get(url_base + input_)

site = BeautifulSoup(response.text, 'html.parser')

product = site.find('div', attrs={"class": "andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated"})

title = product.find('h2', attrs={"class": "ui-search-item__title ui-search-item__group__element"})

link = product.find('a', attrs={"class": "ui-search-link"})

#print(product.prettify())
#print('Título do produto:', title.text)
print('link do produto: ', link['href'])
