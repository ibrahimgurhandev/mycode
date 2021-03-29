heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
}


while True:
    char_name = input("Which character do you want to know about? (wolverine, harry Potter, agent fitz)")
    if char_name in heroes.keys():
      break
    print("Invalid name entered")
while True:
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")
    if char_stat in heroes[char_name].keys():
      break
    print("Invalid stat entered")

print(f"{char_name.capitalize()}'s {char_stat} is: {heroes[char_name][char_stat]}")