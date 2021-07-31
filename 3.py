import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument
from pymongo.errors import ConnectionFailure

db_client = MongoClient()
my_db = db_client.cursos
my_posts = my_db.posts


def buscar(string, substring):
    return string.find(substring, string.find(substring) + 1)


def buscarEncima(string, substring):
    return string.find(substring, string.find(substring))


response = requests.get("https://www.nytimes.com/")
soup = BeautifulSoup(response.content)

Contenidos = []
Provider = []
Duration = []
Start_Date = []
Offered_By = []
No_Of_Reviews = []
Rating = []
ListSearch = []

titulos = soup.find_all("h3", class_="css-xxaj7r e1lsht870")
contenido = soup.find_all("p", class_="css-oemrl2")

extracted = []
for element in contenido:
    element = str(element)
    limpio = str(element[buscarEncima(element, '>') + 1:buscar(element, '<')])
    ListSearch.append({"Content": limpio.strip()})

CLIENT = MongoClient("mongodb://localhost:27017/")
try:
    CLIENT.admin.command('ismaster')
    print('Conexión exitosa')
except ConnectionFailure as fail:
    print('Error al conectar', fail)
db = CLIENT["olimpiadas"]
juegos = db["olimpiadas"]

insertar = juegos.insert_many(ListSearch)