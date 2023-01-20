from app import app
from flask import render_template, request, redirect, url_for
from .forms import UserCreationForm
import requests as r

@app.route('/', methods=['GET', 'POST'])
def findpokemon():
    poke = UserCreationForm()
    if request.method == 'POST':
        url = f'https://pokeapi.co/api/v2/pokemon/{poke.choose.data}'
        response = r.get(url)
        if response.ok:
            # print(my_dict)
            my_dict = response.json()
            pokemon_dict = {}
            pokemon_dict["Name"] = my_dict["name"]
            pokemon_dict["Ability"] = my_dict["abilities"][0]["ability"]["name"]
            pokemon_dict["Base XP"] = my_dict["base_experience"]
            pokemon_dict["Front Shiny"] = my_dict["sprites"]["front_shiny"]
            pokemon_dict["Base ATK"] = my_dict["stats"][1]["base_stat"]
            pokemon_dict["Base HP"] = my_dict["stats"][0]["base_stat"]
            pokemon_dict["Base DEF"] = my_dict["stats"][2]["base_stat"]
        else:
            return "The pokemon you're looking for does not exist."

        return render_template('index.html', poke = poke, pokemon_dict = pokemon_dict)
    
    return render_template('index.html', poke = poke)





