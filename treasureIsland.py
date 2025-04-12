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

user_action = input("Which way would you like to go, right or left?")

if user_action == "right" or user_action == "Right":
    print("You've fallen off a cliff, the game is over")
elif user_action =="left" or user_action == "Left":
    user_action2 = input("Would you like to swim or wait?")
    if user_action2 == "Swim" or user_action2 ==  "swim":
        print("You've been eaten by a shark")
    elif user_action2 =="Wait" or user_action2 == "wait":
        user_action3 = input("Which Door Would You Choose? Red, Blue, or Yellow")
        if user_action3 == "Red" or user_action3 == "red":
            print("You died, game over")
        elif user_action3 == "Blue" or user_action3 == "blue":
            print("Try again, game over")
        elif user_action3 =="yellow" or user_action3 == "Yellow":
            print("You Win!! Great Job")
    else:
        print("Game Over")
else:
    print("You aren't playing correctly")



