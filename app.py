from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def inicio():
    print("holas")
    respuesta = requests.get("https://rickandmortyapi.com/api/character")
    datos = respuesta.json()
    personajes = datos["results"]
    #personajes_nombre = resultado["name"]
    #personajes_especie = resultado["species"]
    return render_template("index.html",datos=datos,personajes = personajes)
