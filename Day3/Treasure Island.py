print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

userSelection = input("The road splits in two ways. Do you continue to the left or to the right? Left or Right \n").lower()
if userSelection == "left":
    #Game Continues
    userSelection = input("You have reached a lake. Will you swim across the lake or wait for the boat to arrive? Swim or Wait \n").lower()
    if userSelection == "wait":
        # Game Continues
        userSelection = input("You have reached a house. Inside it you see 3 different doors. Which are you choosing the Red, Yellow or Blue door? Red or Yellow or Blue \n").lower()
        if userSelection == "yellow":
            #Won
            print("YOU WIN! \nYou have found the long forgotten treasure!")
        elif userSelection == "blue":
            print("GAME OVER \nYou entered the room and the door closed automatically, beasts entered the rom and you were eaten alive.")
        elif userSelection == "red":
            print("GAME OVER \nYou entered a dark room which was lighten by fire and you were burned alive.")
        else:
            print("GAME OVER \nNo one knows which door you selected and you were lost in the fabric of time.")

    elif userSelection == "swim":
        print("GAME OVER \nYou were attacked by trout.")
    else:
        print("GAME OVER\nYou were cursed and forgot where you are and what are you are doing.")
elif userSelection == "right":
    print("GAME OVER \nYou have fallen into a deep hole you cannot escape.")

else:
    print("GAME OVER\nYou took the adventures route of nowhere and you were lost in the forest.")