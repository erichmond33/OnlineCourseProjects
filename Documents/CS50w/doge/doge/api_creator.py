import random
import copy
import json

#import image_blender


'''
backgrounds = ["black", "purple", "green"]

bodies = ["pink", "scales", "toasted"]

eyes = ["angry", 'watery', "high"]

clothes = ["thriller", "jacket", "t-shirt"]

mouths = ["tape", "vape", "blunt"]

hats = ["pirate", "sailor", "pope"]

ears = ["big", "small", "earring"]

api =   {
        "name": "Wicked Cranium #4102",
        "image": "https://bafkreibpafeorxg67r3mczps4ekpto46q6rznnnpxdd5gcsnbbsmezpvom.ipfs.dweb.link",
        "attributes": [
            {
            "trait_type": "Background",
            "value": "Never none"
            },
            {
            "trait_type": "Eyes",
            "value": "None"
            },
            {
            "trait_type": "Extra",
            "value": "None"
            },
            {
            "trait_type": "Clothes",
            "value": "None"
            },
            {
            "trait_type": "Head",
            "value": "None"
            },
            {
            "trait_type": "Mouth",
            "value": "None"
            }
        ]
        }

api_list = []

for x in range(10000):


    api["name"] = f"Avant-Garde #{x}"

    api["attributes"][0]["value"] = random.choice(backgrounds)

    api["attributes"][1]["value"] = random.choice(bodies)

    api["attributes"][2]["value"] = random.choice(eyes)

    api["attributes"][3]["value"] = random.choice(clothes)

    api["attributes"][4]["value"] = random.choice(hats)

    api["attributes"][5]["value"] = random.choice(mouths)

    api["attributes"][6]["value"] = random.choice(ears)

    api_list.append(copy.deepcopy(api))

num = 0

for file in api_list:

    if file["attributes"][0]["value"] == "black":
        num+=1

print(num)


#print(api)

'''
nof_trait_counts = {5:0,4:0,3:0}
nof_traits = {"Eyes":0,"Extras":0,"Clothes":0,"Heads":0,"Mouths":0}



api =   {
        "name": "Wicked Cranium #4102",
        "image": "https://bafkreibpafeorxg67r3mczps4ekpto46q6rznnnpxdd5gcsnbbsmezpvom.ipfs.dweb.link",
        "attributes": [
            {
            "trait_type": "Background",
            "value": "Never none"
            },
            {
            "trait_type": "Eyes",
            "value": "None"
            },
            {
            "trait_type": "Extra",
            "value": "None"
            },
            {
            "trait_type": "Clothes",
            "value": "None"
            },
            {
            "trait_type": "Head",
            "value": "None"
            },
            {
            "trait_type": "Mouth",
            "value": "None"
            }
        ]
        }


backgrounds = ["White", "Red", "Blurple", "Green", "Dingy Yellorange", "Light Blue", "Purple", "Rainbow", "Pink", "Too Loud"]
extras = ["Get Hard", "69", "Mike Tyson", "Illuminate", "Prank", "Sniper", "Harry", "Eye Black", "Airpods", "Ranch It Up","Swords"]
clothes = ['Stratton', 'Rick Rolled', 'Bandolier', 'Bake',
'Original', 'Thriller', 'Spaceman', 'Crocodile Hunter', 
'Lloyd', 'Swamp People', 'Thrift Shop', 'Denim Jacket',
'The Champ Champ', 'Shake', 'Doge To the Moon', 'Nacho',
'Major Payne', 'Terminator', 'Snakeskin', "Cowboy", 'Hotrod', 'McLovin',
'Harambe', "Magnum Dong", "Fluffy", "DONKEY", "Burgundy", "Carlos", "McCracken",
"Gravey Train", "Idiot Sandwhich", "Insertchucknorrisjokehere", "Tropic Thunder",
"Wilder", "Wubba Lubba Dub Dub", "Houdini"]
heads = ['Wolverine Hat', 'Planet BS', "The Best Pirate I Have Ever Seen", "Indiana Jones",
"Turds", "Hulk Hogan", "King George", "Angus Young", "Clint Eastwood",
"Wildcat", "Alright", "Eminem", "Santa", "Joker", "Army", "Dino",
"Wolverine", "Tinfoil", "Wax On Wac Off", "Happy Accidents", "Date Mike", "Clark",
"Somebody Stop Me", "Sombrero", "Classic Bowler", "Captain", "Nobody Cares", "Ducks", "Watermelon"]
eyes = ["Wilder", "No Eyes", "Thug Life", "Lazers", "Aviators",
"Rocketman", "Purple", "Undertaker", "Eyepatch", "Wolfie", "All Knowing",
"Jackass 3d", "Unistyle", "Truly Unfortunate", "What If I Told You",
"Wack", "Eyeliner", "Lines"]
mouths = ["Snoop Dogg", "Sun Tzu", "Tape", "Leonardo", "Pipe",
"Hunger Games", "Toothpick", "Piercing", "Speechless", "Sam Elliot",
"Mutton Chops", "I Can Quit Whenever I Want", "Straw", "Shiv",
"Bull Ring", "Pucker Up"]

api_list = []
trait_counts = [5,4,3]
total_individual_traits = int(len(extras)) + int(len(clothes)) + int(len(heads)) + int(len(eyes)) + int(len(mouths))


for x in range(1156):
    #Give it a name
    api["name"] = f"Avant-Garde #{x + 5814}"
    #Give it a background
    api["attributes"][0]["value"] = random.choice(backgrounds)
    # Reset API Traits
    api["attributes"][1]["value"] = "None"
    api["attributes"][2]["value"] = "None"
    api["attributes"][3]["value"] = "None"
    api["attributes"][4]["value"] = "None"
    api["attributes"][5]["value"] = "None"

    #Determine how many traits it gets
    trait_count = random.choices(trait_counts, weights=(25, 50, 25))

    if trait_count == [5]:
        nof_trait_counts[5] += 1
    elif trait_count == [4]:
        nof_trait_counts[4] += 1
    else:
        nof_trait_counts[3] += 1


    traits = ["eyes", "extras", "clothes", "heads", "mouths"]
    trait_weights = [len(eyes) / total_individual_traits, len(extras) / total_individual_traits, len(clothes) / total_individual_traits, len(heads) / total_individual_traits, len(mouths) / total_individual_traits]
    selections = []

    #Loop over the number of traits
    for trait in range(trait_count[0]):

        selection = random.choices(traits, trait_weights)
        selections.append(selection[0])

        if selection == ["eyes"]:
            trait_weights[0] = 0

            api["attributes"][1]["value"] =  random.choice(eyes)
            nof_traits["Eyes"] += 1
        elif selection == ["extras"]:
            trait_weights[1] = 0

            api["attributes"][2]["value"] =  random.choice(extras)
            nof_traits["Extras"] += 1
        elif selection == ["clothes"]:
            trait_weights[2] = 0

            api["attributes"][3]["value"] = random.choice(clothes)
            nof_traits["Clothes"] +=1
        elif selection == ["heads"]:
            trait_weights[3] = 0

            api["attributes"][4]["value"] =  random.choice(heads)
            nof_traits["Heads"] +=1
        elif selection == ["mouths"]:
            trait_weights[4] = 0

            api["attributes"][5]["value"] =  random.choice(mouths)
            nof_traits["Mouths"] += 1

    api_list.append(copy.deepcopy(api))
    #print(selections)



with open("api_list2.json", "w") as outfile:
        json.dump(api_list, outfile, indent=4)

#image_blender.run()

#print(f"TRAIT WEIGHTS: {[len(eyes) / total_individual_traits, len(extras) / total_individual_traits, len(clothes) / total_individual_traits, len(heads) / total_individual_traits, len(mouths) / total_individual_traits]}")
#print(f"NUMBER OF TRAIT COUNTS: {nof_trait_counts}")
#print(f"NUMBER OF TRAITS: {nof_traits}")
        


