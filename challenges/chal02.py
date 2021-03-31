farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def animals_from_ne_farm():
    for animal in farms[0]["agriculture"]:
        print(animal)
animals_from_ne_farm()

def choose_farm():
    farm_chosen = input("what farm will you like to look at: NE Farm, W Farm or SE Farm: ").upper()
    for item in farms:
        if farm_chosen in item["name"]:
            for animal in item["agriculture"]:
                print(animal)
choose_farm()

def choose_farm_return_animals_only():
    farm_chosen = input("what farm will you like to look at: NE, W or SE: ").upper()
    for item in farms:
        if farm_chosen in item["name"]:
            for animal in item["agriculture"]:
                if animal not in {"carrots", "celery"}:
                    print(animal)
choose_farm_return_animals_only()






