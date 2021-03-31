#!/usr/bin/env python3

import requests

def main():
    """Run time code"""
    r = requests.get('https://cat-fact.herokuapp.com/facts').json()

    for catfact in r:
        print(catfact.get("text"))
main()

