import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
# Para cada arquivo, siga cada link, encontre a imagem e faça download
# Download fotos: urllib
# Parse e tratamento HTML: BeautifulSoup

# Links
index_page = 'https://apod.nasa.gov/apod/archivepix.html'
pasta_downloads = 'Exercises/WebCrawler/apod_pictures'
print("Index: " + index_page)
# Traz todo o HTML
conteudo = urllib.request.urlopen(index_page).read()


# Cria objeto bs4 que contem todos as tags a
for link in BeautifulSoup(conteudo, "html.parser").findAll("a"):
    # Converter url relativa para absoluta
    href = urljoin(index_page, link['href'])

    # Traz o conteudo do novo link, para extrair a imagem
    conteudo = urllib.request.urlopen(href).read()

    for img in BeautifulSoup(conteudo, "html.parser").findAll("img"):
        img_href = urljoin(href, img["src"])

        # Download Imagens
        print("Downloading image: " + img_href)
        image_name = img_href.split("/")[-1]
        # print(image_name)

        caminho = os.path.join(pasta_downloads, image_name)
        # print(caminho)
        urllib.request.urlretrieve(img_href, caminho)
