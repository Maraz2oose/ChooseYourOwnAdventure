name = "YourNameHere"
#this is the intro code

print(f"Hello and welcome to {name} Game of games!\nas you follow along in this story you will be presented with choices that will decide your fate! lets begin")


#First Choice

print("You are in a dark room after searching around for a bit you find yourself in front of two doors.\none is a old red door with wear and tear, the other is a sleek modern white door. which do you go through?")


#question

DoorChoice = input("Which Door do you choose do go into? red=red door or white=white door\n")


#Red door code


if DoorChoice == "red":
    print("You walk through the beat up old door and stumble into a barn. there is an old man working and he seems like he is in trouble.")

    Helpman = input("Do you help the struggling old man with his dutys or walk off in the distance? 1=help or 2=walk away \n")

    if Helpman== "1":
        print("You help out the old man and he is extremely grateful, he asks where you come from and you just say your lost.\n he offers you a job at his farm and a place in his house. you end up taking up the offer and live hapilly with the old man")


    else:
        print(""" ____________ GAME OVER ____________
        Too bad! you walk off into the distance regretting your descision and eventually bite the dust """)
 #white door code
else:
    print("You walk through the white door, and realize that you have stumbled into the future.\n you see a scientist and he asks whats wrong, you answer that you are lost in time.\n he offers to take you back to the present in his time machine.")

    Accept = input("Do you Accept? 1=Yes 2=No")

    if Accept== "1":
        print("The Scientist takes you back in time to your house and you live happily ever after")

    else:
        print("Why wouldnt you take up that offer? your now stuck in the future, without a family or home.")

