#!/usr/bin/env python3
import random
import requests

def main():
    """Run time code"""
    city = input("what city do you live in?: ")
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=003bd0423f8f627a496637434f9231df').json()

    print(r["weather"][0]["description"])
main()

