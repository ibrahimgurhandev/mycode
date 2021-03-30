#!/usr/bin/env python3
#
# heroes=  {
# "wolverine":
#     {"real name": "James Howlett",
#     "powers": "regeneration",
#     "archenemy": "Sabertooth",},
# "harry potter":
#     {"real name": "Harry Potter",
#     "powers": "he's a wizard",
#     "archenemy": "Voldemort",},
# "agent fitz":
#     {"real name": "Leopold Fitz",
#     "powers": "intelligence",
#     "archenemy": "Hydra",}
# }
#
#
# while True:
#     char_name = input("Which character do you want to know about? (wolverine, harry Potter, agent fitz)")
#     if char_name in heroes.keys():
#       break
#     print("Invalid name entered")
# while True:
#     char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")
#     if char_stat in heroes[char_name].keys():
#       break
#     print("Invalid stat entered")
#
# print(f"{char_name.capitalize()}'s {char_stat} is: {heroes[char_name][char_stat]}")
#
#
# My eyes! The goggles do nothing!

# challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
# print(f"My {challenge[2][-1]}! The {challenge[2][0]} do {challenge[-1]}!")
#
# trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
# print(f'My {trial[2].get("goggles")}! The {trial[2].get("eyes")} do {trial[-1]}!')
#
# nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
# print(f'My {nightmare[0]["user"]["name"]["first"]}! The {nightmare[0]["kumquat"]} do {nightmare[0]["d"]}!')
