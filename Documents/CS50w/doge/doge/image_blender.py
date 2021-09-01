from PIL import Image
import numpy as np
import pin
import json
import os

def run():

    with open('api_list3.json') as json_file:
        api_list = json.load(json_file)

    #These lists determine how much hair the body has
    one = ["Wolverine Hat", "Planet BS", "Dino", "Wax On Wac Off", "Nobody Cares", "Ducks", "None"]
    two = ["King George", "Turds", "Angus Young", "Wildcat", "Santa", "Army", "Wolverine", "Happy Accidents", "Date Mike", "Clark", "Somebody Stop Me", "Sombrero", "Classic Bowler", "Captain", "Watermelon"]
    three = ["Clint Eastwood", "Alright", "Eminem", "Joker", "Tinfoil", "The Best Pirate I Have Ever Seen"]
    four = ["Indiana Jones", "Hulk Hogan"]

    increment = 0

    for api in api_list:

        #Getting all of the images from the API
        background_path = api['attributes'][0]["value"].replace(" ", "_")
        eye_path = api['attributes'][1]["value"].replace(" ", "_")
        extra_path = api['attributes'][2]["value"].replace(" ", "_")
        clothes_path = api['attributes'][3]["value"].replace(" ", "_")
        head_path = api['attributes'][4]["value"].replace(" ", "_")
        mouth_path = api['attributes'][5]["value"].replace(" ", "_")

        background_img = Image.open(f"./static/doge/attributes/backgrounds/background_{background_path}.png")
        eye_img = Image.open(f"./static/doge/attributes/eyes/eyes_{eye_path}.png")
        extra_img = Image.open(f"./static/doge/attributes/skins/extras_{extra_path}.png")
        clothes_img = Image.open(f"./static/doge/attributes/bodies/body_{clothes_path}.png")
        head_img = Image.open(f"./static/doge/attributes/heads/head_{head_path}.png")
        mouth_img = Image.open(f"./static/doge/attributes/mouths/mouth_{mouth_path}.png")

        if api['attributes'][4]["value"] in one:
            body_img = Image.open(f"./static/doge/attributes/rick1.png")
        elif api['attributes'][4]["value"] in two:
            body_img = Image.open(f"./static/doge/attributes/rick2.png")
        elif api['attributes'][4]["value"] in three:
            body_img = Image.open(f"./static/doge/attributes/rick3.png")
        elif api['attributes'][4]["value"] in four:
            body_img = Image.open(f"./static/doge/attributes/rick4.png")


        #This is the normal order for making a picture
        def normal_order():
            background_img.alpha_composite(body_img)
            background_img.alpha_composite(extra_img)
            background_img.alpha_composite(eye_img)
            background_img.alpha_composite(clothes_img)
            background_img.alpha_composite(head_img)
            background_img.alpha_composite(mouth_img)

            background_img.save("new.png", "PNG")

        #This is the order if the eyes are lazers
        def lazer_order():
            background_img.alpha_composite(body_img)
            background_img.alpha_composite(extra_img)
            background_img.alpha_composite(clothes_img)
            background_img.alpha_composite(head_img)
            background_img.alpha_composite(mouth_img)
            background_img.alpha_composite(eye_img)

            return background_img

        def hair_and_glasses_order():
            background_img.alpha_composite(body_img)
            background_img.alpha_composite(extra_img)
            background_img.alpha_composite(clothes_img)
            background_img.alpha_composite(head_img)
            background_img.alpha_composite(eye_img)
            background_img.alpha_composite(mouth_img)

            return background_img

        def beard_and_helmet_order():
            background_img.alpha_composite(body_img)
            background_img.alpha_composite(extra_img)
            background_img.alpha_composite(clothes_img)
            background_img.alpha_composite(mouth_img)
            background_img.alpha_composite(eye_img)
            background_img.alpha_composite(head_img)

            return background_img

        def beard_and_helmet_and_lazers_order():
            print("beard")
            background_img.alpha_composite(body_img)
            background_img.alpha_composite(extra_img)
            background_img.alpha_composite(clothes_img)
            background_img.alpha_composite(mouth_img)
            background_img.alpha_composite(head_img)
            background_img.alpha_composite(eye_img)

            return background_img

        def beard_and_helmet_and_glasses_order():
            background_img.alpha_composite(body_img)
            background_img.alpha_composite(extra_img)
            background_img.alpha_composite(clothes_img)
            background_img.alpha_composite(mouth_img)
            background_img.alpha_composite(head_img)
            background_img.alpha_composite(eye_img)
            

            return background_img


        glasses = ["Wilder", "Thug Life", "Aviators", "Rocketman", "Wolfie", "Jackass 3d", "What If I Told You"]
        hair = ["Hulk Hogan", "Joker", "Wolverine", "Wax On Wac Off", "Happy Accidents", "Eminem"]

        helmets = ["Wildcat", "Wolverine Hat", "Wolverine", "Joker", "Happy Accidents", "Watermelon", "Angus Young", "Eminem"]
        beards = ["Mutton Chops", "Hunger Games"]


        if api['attributes'][1]["value"] == "Lazers":
            if (api['attributes'][5]["value"] in beards) and (api['attributes'][4]["value"] in helmets):
                beard_and_helmet_and_lazers_order()
            else:
                lazer_order()
        elif (api['attributes'][1]["value"] in glasses) and (api['attributes'][4]["value"] in hair):
            if (api['attributes'][5]["value"] in beards) and ((api['attributes'][4]["value"] in helmets or api['attributes'][1]['value'] in glasses)):
                beard_and_helmet_and_glasses_order()
            else:
                hair_and_glasses_order()
        elif (api['attributes'][5]["value"] in beards) and ((api['attributes'][4]["value"] in helmets or api['attributes'][1]['value'] in glasses)):
            print("butt")
            beard_and_helmet_order()
        elif (api['attributes'][1]["value"] == "Eyepatch" and api['attributes'][4]["value"] == "Hulk Hogan"):
            eye_img = Image.open(f"./static/doge/attributes/eyes/eyes_Eyepatch2.png")
            normal_order()
        else:
            normal_order()


        #background_img.save(f"{increment}.png", "PNG")
        background_img.save("new.png", "PNG")
        
        #hash = pin.pin_img(f"{increment}.png")
        hash = pin.pin_img(f"new.png")
        hash = hash[0:46].decode('utf-8')
        
        api["image"] = f"https://ipfs.io/ipfs/{hash}"

        with open("api_list3.json", "w") as outfile:
            json.dump(api_list, outfile, indent=4)

        print(increment)
        increment += 1
        
        #os.remove(f"{increment}.png")

run()
