import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','news.settings')

import django
django.setup()

from noticias.models import Webscrapy

site = "https://www.tecmundo.com.br/" #define o site para fazer scaping
page = requests.get(site) #baixa a pagina 
soup = BeautifulSoup(page.text, 'html.parser') #define o soup
#começa o scraping na pagina 
title_carousel= soup.find_all('a',class_="tec--carousel__item__title__link") #pega os links em destaques
title_cards= soup.find_all('a',class_="tec--card__title__link") #links secundarios
for link in title_carousel: #organiza e salva no banco os titulos em destaque
	title=link.get_text()#extrai o titulo
	print(title)#exibe na tela os links que esta sendo salvo
	fonte=link.get("href") # extrai a fonte (link)
	store=Webscrapy(title=str(title),description=str(fonte))
	store.save()#seta no banco

for link in title_cards:#organiza e salva no banco os titulos secundarios
	title=link.get_text()#extrai o titulo
	print(title)#exibe na tela os links que esta sendo salvo
	fonte=link.get("href")
	store=Webscrapy(title=str(title),description=str(fonte))
	store.save()
	
	