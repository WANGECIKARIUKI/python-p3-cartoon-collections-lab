def roll_call_dwarves(dwarves):
    dwarves = [f'{dwarf[0]}. {dwarf[1]}' for dwarf in enumerate(dwarves,1)]
    for dwarf in dwarves:
        print(dwarf)
# dwarf names ["Doc", "Dopey", "Bashful", "Grumpy"]

def summon_captain_planet(planeteer):
    planeteer_calls = [f'{planet.title()}!' for planet in planeteer]
    return planeteer_calls
#planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def long_planeteer_calls(planeteer):
    planeter_calls = [True for planet in planeteer if len(planeteer) > 4]
    if planeter_calls:
        return False
    else:
        return True

def find_the_cheese(list):
    cheese = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
    

    for item in list:
        if item in cheese:
            print(item)
    return None 

# find_the_cheese(["crackers", "gouda", "thyme"])
find_the_cheese(["tomato soup", "cheddar", "oyster crackers", "gouda"])