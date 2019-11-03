# Django_phython_websracpping
#Projeto visa fazer o webscraping na pagina do tecmundo salvando as noticias que estão na primeira pagina no banco de dados sqllite3.

#Segue alguns comandos utilizados:

#instalação do virtualenv python3
apt-get install python3-pip
python3.7 -m venv venv

#ativar o virtualenv
source venv/bin/activate

criando projeto no django django 
django-admin startproject noticias

#adicionando os models

python manage.py makemigrations
python manage.py migrat

#starta django
python manage.py runserver

#instalando a beatifull soup
pip3 install BeautifulSoup4

Obs: todas as dependecias do projeto esta no requirements.txt
