import requests
from bs4 import BeautifulSoup
response = requests.get('https://g1.globo.com/')

content = response.content  # formato "bytes"

site = BeautifulSoup(content, 'html.parser')  # [1] formato do conteúdo

# HTML da notícia
noticia = site.find('div', attrs={'class': "feed-post-body"})  # attrs atributos html | find encontra o primeiro atributo com a especificação passada

#print(noticia.prettify())  # prettify melhora a visualização

# Título
titulo = noticia.find('a', attrs={"class": "feed-post-link gui-color-primary gui-color-hover"})

#print(titulo)

# Subtítilo
subtitulo = noticia.find('a', attrs={"class": "gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext"})

print(subtitulo.text)
