print("Welcome to treasure Island!.\nYour mission is to find the treasure")
cross_road = input("You're at a crossroad.where do you want to go? Type 'left' or 'right'? ")
if cross_road == "left":
    print("You came to a lake")
    lake =input("'wait' or 'swim'? ")
    if lake == "wait":
        print("You have reached a 3 doors.")
        door=input("What color door you choose red,blue,yellow?  ")
        if door == "red":
            print("Burned by fire.Game over!")
        elif door == "blue":
            print("Eaten by beats.Game over!")
        elif door == "yellow":
            print("YOU WIN!!!")
        else:
            print("GAME OVER!")                      
    else:
        print("Attacked by trout.Game over!")

else:
    print("Fall into a hole.Game over!")    

