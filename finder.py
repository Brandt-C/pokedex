print('Welcome to Pokedex!  ')
while True:
    choice = input('What pokemon are you looking for?  Type "quit" to exit.  ')
    if choice.lower() == 'quit':
        print('Thank you for using Pokedex!  ')
        break
    else:
        url = f'https://pokeapi.co/api/v2/pokemon/{choice.lower()}'
        response = requests.get(url)
        if response.ok:
            response = requests.get(url)
            data = response.json()
            pokemon = [data['name'], data['abilities'][0]['ability']['name'], data['base_experience'], data['sprites']['front_shiny'], data['stats'][1]['base_stat'], data['stats'][0]['base_stat'], data['stats'][2]['base_stat']]
            print(f'Name:  {pokemon[0]}  \nAbility:  {pokemon[1]}  \nBase Experience:  {pokemon[2]}  \nImage:  {pokemon[3]}  \nAttack Base Stat:  {pokemon[4]}  \nHP Base Stat:  {pokemon[5]}  \nDefense Base Stat:  {pokemon[6]}\n')
        else:
            print('Invalid entry.  Please try again.  ')




        {{ form.hidden_tag() }} 

        {{ form.choice(class='form-control', placeholder = 'Choose Your Pokemon!') }}
 
        {{ form.submit(class='btn btn-primary') }}


    {{ choice.hidden_tag() }} 

    {{ choice.username(class='form-control', placeholder = 'Username') }}

    {{ choice.submit(class='btn btn-primary') }}
