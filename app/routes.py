from app import app
from flask import render_template, request, redirect, url_for
from .forms import UserCreationForm
import requests as r

@app.route('/index', methods=['GET', 'POST'])
@app.route('/')
def findpokemon():
    poke = UserCreationForm()
    url = f'https://pokeapi.co/api/v2/pokemon/pikachu'
    response = r.get(url)
    my_dict = response.json()
    if response.ok:
        # print(my_dict)
        pokemon = [my_dict['name'], my_dict['abilities'][0]['ability']['name'], my_dict['base_experience'], my_dict['sprites']['front_shiny'], my_dict['stats'][1]['base_stat'], my_dict['stats'][0]['base_stat'], my_dict['stats'][2]['base_stat']]
        image = pokemon[3]
        info = (f'Name:  {pokemon[0]}\n  Ability:  {pokemon[1]}  \nBase Experience:  {pokemon[2]}  \nAttack Base Stat:  {pokemon[4]}  \nHP Base Stat:  {pokemon[5]}  \nDefense Base Stat:  {pokemon[6]}\n')
    else:
        return "The pokemon you're looking for does not exist."

    return render_template('index.html', poke = poke, pokemon = pokemon, info = info, image=image)




