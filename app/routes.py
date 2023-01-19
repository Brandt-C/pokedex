from app import app
from flask import render_template, request, redirect, url_for
from .forms import UserCreationForm
import requests 

@app.route('/index')
@app.route('/')
def homePage():

    form = UserCreationForm()
    choice = form.choice.data
    url = f'https://pokeapi.co/api/v2/pokemon/ditto'
    response = requests.get(url)
    if response.ok:
        response = requests.get(url)
        poke = response.json()

    pokemon = [
        poke['name'], 
        poke['abilities'][0]['ability']['name'], 
        poke['base_experience'], 
        poke['sprites']['front_shiny'], 
        poke['stats'][1]['base_stat'], 
        poke['stats'][0]['base_stat'], 
        poke['stats'][2]['base_stat']
        ]


    return render_template('index.html', pokemon = pokemon)




