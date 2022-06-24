# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup

print()

url_base = 'https://lista.mercadolivre.com.br/'

input_ = str(input('Digite o nome do produto: '))

response = requests.get(url_base + input_)

site = BeautifulSoup(response.text, 'html.parser')

products = site.findAll('div', attrs={"class": "andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated"})

for product in products:

    title = product.find('h2', attrs={"class": "ui-search-item__title ui-search-item__group__element"})

    link = product.find('a', attrs={"class": "ui-search-link"})

    value1 = product.find('div', attrs={"class": "ui-search-price__second-line"})
    value2 = product.find('span', attrs={"class": "price-tag-fraction"})

    cents = product.find('span', attrs={"class": "price-tag-cents"})

    if (cents):
        print('\033[1;43mTítulo do produto:\033[m', title.text)

        print('\033[1;43mlink do produto:\033[m', link['href'])

        print('\033[1;43mO valor é: R$\033[m', value2.text,',', cents.text)

        print("\n\n")

    else:
        print('\033[1;43mTítulo do produto:\033[m', title.text)

        print('\033[1;43mlink do produto:\033[m', link['href'])

        print('\033[1;43mO valor é: R$\033[m', value2.text,',00')

        print("\n\n")

        # salvar os preços em um dataframe!!! 
        # usar pandas




#print(product.prettify())