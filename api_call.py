# How to connect to API using python
import requests
base_url = "https://pokeapi.co/api/v2/"
def pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retreive data ERROR:{response.status_code}")
    
pokemon_name = input("Enter the pokemon name: ").lower()
pokemon_details = pokemon_info(pokemon_name)

if pokemon_details:
    print(f"Name: {pokemon_details["name"].capitalize()}")
    print(f"ID: {pokemon_details["id"]}")
    print(f"Height: {pokemon_details["height"]}")
    print(f"Weight: {pokemon_details["weight"]}")