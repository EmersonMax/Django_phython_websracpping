import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','news.settings')

import django
django.setup()

from noticias.models import Webscrapy

page = requests.get("https://www.tecmundo.com.br/")
soup = BeautifulSoup(page.text, 'html.parser')
#print(page)
#print(soup.prettify())
#list(soup.children)
title_carousel= soup.find_all('a',class_="tec--carousel__item__title__link")
title_cards= soup.find_all('a',class_="tec--card__title__link")
for link in title_carousel:
	title=link.get_text()
	store=Webscrapy(title=str(title),description=str(link))
	store.save()


for link in title_cards:
	title=link.get_text()
	print(title)
	store=Webscrapy(title=str(title),description=str(link))
	store.save()
	