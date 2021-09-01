import random
import copy

skins = ["Teardrops", "69", "Mike Tyson", "Skull", "Illuminate"]

clothes = ['Stratton', 'Rick Rolled', 'Bandolier', 'Bake',
'Original', 'Thriller', 'Space Suit', 'Steve Erwin', 
'Lloyd', 'Deniem Overalls', 'Thrift Shop', 'Deniem Jacket',
'The Champ', 'Shake', 'Doge to the moon', 'Nacho',
'Major Payne', 'Terminator', 'Snakeskin', "Cowboy", 'Hotrod', 'Mclovin',
'BAYC']

hats = ['Wolverine Hat', 'Icepack', "Jack Sparrow", "Indiana Jones",
"Major Payne", "Hulk Hogan", "King George", "Angus Young", "Clint Eastwood",
"Wildcat", "Alright", "Eminem", "Santa", "Joker", "Army", "Dino",
"Wolverine", "Tinfoil"]

eyes = ["Wilder", "No Eyes", "Thug Life", "Lazers", "Aviators",
"Elton", "Purple", "White", "Eyepatch", "Wolfie", "All Knowing",
"Jackass 3d"]

#backgrounds = ["None", "Red", "Blue", "Green", "Yellow", "Light Blue", "Purple", "Rainbow"]

ears = ["Axe", "Diamond Stud"]

mouths = ["Snoop", "Sun Tzu", "Tape", "Leonardo", "Pipe",
"Hunger Games", "Toothpick"]


traits = ["skins", "clothes", "hats", "eyes", "ears", "mouths"]

trait_counts = [7,7,7]

total_length = int(len(skins)) + int(len(clothes)) + int(len(hats)) + int(len(eyes)) + int(len(ears)) + int(len(mouths))
print(total_length)

skins_ = 0
clothes_ = 0
hats_ = 0
eyes_ = 0
ears_ = 0
mouths_ = 0

six = 0
five = 0
four = 0

for x in range(10000):

    trait_count = random.choices(trait_counts, weights=(25, 50, 25))

    already_selected = []
    
    for x in trait_count:

        if len(already_selected) == 0:
            trait = random.choices(traits, weights=(len(skins)/ total_length, len(clothes)/ total_length, len(hats)/ total_length, len(eyes)/ total_length, len(ears)/ total_length, len(mouths)/ total_length))
        else:
            trait = random.choices(traits, weights=(len(skins)/ total_length, len(clothes)/ total_length, len(hats)/ total_length, len(eyes)/ total_length, len(ears)/ total_length, len(mouths)/ total_length))
            while trait not in already_selected:
                trait = random.choices(traits, weights=(len(skins)/ total_length, len(clothes)/ total_length, len(hats)/ total_length, len(eyes)/ total_length, len(ears)/ total_length, len(mouths)/ total_length))


        already_selected.append(trait)

        if trait == ['skins']:
            skins_ += 1
        elif trait == ['clothes']:
            clothes_ +=1
        elif trait == ["hats"]:
            hats_ +=1
        elif trait == ["eyes"]:
            eyes_ +=1
        elif trait == ["ears"]:
            ears_ +=1
        elif trait == ["mouths"]:
            mouths_ +=1

    

    
    if trait_count == [6]:
        six += 1
    elif trait_count == [5]:
        five += 1
    else:
        four += 1


print(six, five, four)
print("\n------------------")
print(len(skins), len(clothes), len(hats), len(eyes), len(ears), len(mouths))
print(skins_, clothes_, hats_, eyes_, ears_, mouths_)
