# Treasure Island - Choose Your Adventure
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

first_step = input("You have arrived on the Treasure Island dock. Treasure, adventure, and danger await. "
                   "Two paths lay before you - right or left?\n").lower()

if first_step == "left":
    second_step = input("You follow the path along through the jungle. The moonlight leads you to a lake. A ferry is "
                        "carrying another treasure seeker to a small island with flickering torches. Should you wait "
                        "for the ferry to return or swim across the dark water - wait or swim?\n").lower()
    if second_step == "wait":
        third_step = input(
            "The ferry has returned and carries you across the dangerous waves to a small cabin set back "
            "off of the shore. There are three doors of varying colors: red, yellow, and blue. Only one "
            "leads to the treasure - red, yellow, or blue?\n").lower()
        if third_step == "yellow":
            print(
                "You walk into an empty room lit by a single candle on a table. A note appears to be tucked under the "
                "candlestick. You read the note and discover the gold is hidden underneath the floorboards! "
                "Congratulations! You've won!")
        elif third_step == "red":
            print(
                "You have entered a dragon's lair and awoken the beast. The beast does not like visitors and has "
                "roasted you for trespassing. Game Over. You lose.")
        elif third_step == "blue":
            print(
                "You have entered a warg cave. They smell you at once and cannot control their hunger. Your light has "
                "been extinguished. Game Over. You lose.")
        else:
            print(
                "You thought you were smart, didn't you? By avoiding the doors altogether you thought you could see "
                "what lies behind the cabin. Unfortunately this island happens to be inhabited by a cannibal zombie "
                "pirate crew who make quick work of you for dinner. Game Over. You lose.")
    elif second_step == "swim":
        print("Today is not the day to swim across these dark, unforgiving waves. The mutant trout are hungry and you "
              "look like dinner. Game over. You lose.")
    else:
        print("You mustn't stray from the jungle path. The creatures that await are more fearsome than any danger that "
              "awaits further ahead. Your life is forfeit. Game over. You lose.")
else:
    print("You have fallen into a deep cavern where evil awaits. Game Over. You lose.")
