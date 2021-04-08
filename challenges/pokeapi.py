#!/usr/bin/env python3
import requests
import wget
import pprint

def main():

    pokemon = input("What pokemon do you want to view\n>").lower()
    pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()
    image_link = pokeapi['sprites']['front_default']
    print(f"here is a link to an image of {pokemon}:", image_link)
    print('Downloading image......................................')
    wget.download(image_link)
    print(f"Number of Game indices for {pokemon} are :", len(pokeapi['game_indices']))
    print(f"Here all of {pokemon}'s special moves :")
    for move in pokeapi['moves']:
        pprint.pprint(move['move']['name'])

main()