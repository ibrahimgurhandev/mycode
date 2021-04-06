#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response

        got_dj = gotresp.json()
        pprint.pprint(got_dj)
        for house in range(len(got_dj['allegiances'])):
            house = requests.get(got_dj['allegiances'][house]).json()
            print(house['name'])

        books = []
        books.extend(got_dj['books'])
        books.extend(got_dj['povBooks'])
        for book in range(len(books)):
            book = requests.get(books[book]).json()
            print(book['name'])




if __name__ == "__main__":
        main()