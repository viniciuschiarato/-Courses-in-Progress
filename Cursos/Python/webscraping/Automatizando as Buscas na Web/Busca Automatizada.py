import openpyxl
import requests
from bs4 import BeautifulSoup
import pandas as pd
lista_noticias = list()

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticias = site.findAll('div', attrs={'class': "feed-post-body"})

# validação
for noticia in noticias:

    # Título
    titulo = noticia.find('a', attrs={"class": "feed-post-link gui-color-primary gui-color-hover"})

    #print(titulo.text)
    #print(titulo['href'])

    # Subtítilo
    subtitulo = noticia.find('a', attrs={"class": "gui-color-primary gui-color-hover feed-post-body-title "
                                                  "bstn-relatedtext"})

    if (subtitulo):
        lista_noticias.append([titulo.text, titulo['href'], subtitulo])
    else:
        lista_noticias.append([titulo.text, titulo['href'], ''])

news = pd.DataFrame(lista_noticias, columns=['Título', 'Link', 'Subtítulo'])

news.to_excel('noticia.xlsx', index=False)

print(news)
