# Text Based Adventure Game!


print("*INTERCOM* Welcome to flight 0322, now departing LAX for Hawaii.")
print("*INTERCOM* Your estimated flight time is approximately 6 hours. Please fasten your seat belt, relax, and enjoy the flight!")
print("As the view of the city fades, you look out of your window to see nothing but empty ocean.")
print("*PLAYER CHOICE: Do you want to WATCH A MOVIE or SCROLL REDDIT? (watch a movie/scroll reddit).")

### Prompt user for first choice

entertainmentChoice = input("> ")

## lower() and strip() ensure player input gets returned as lowercase and with no spaces

if(entertainmentChoice.lower().strip() == "watch a movie"):
    print("It's a Christmas movie. A cookie-cutter premise about a male protagonist from The City who has to go to The Country for his prestigious work and falls in love with a girl from The Country.")
    print("-----")
    print("You fall asleep...")
    
elif(entertainmentChoice.lower().strip() == "scroll reddit"):
    print("You search reddit for which programming language will land you a sweet job the fastest. You are annoyed at not being able to land a six figure job immediately and close reddit.")
    print("-----")
    print("You fall asleep")
    
else: 
    print("Please choose (watch a movie) or (scroll reddit)")


#importing time module
import time

time.sleep(2)
print("-----")
print("zzZZzzZZZZzzzz")
time.sleep(2)

print(" ")
print(" ")
print("-----")
print(" ")
print(" ")

def press_enter_to_continue():
    input("[ENTER] Press enter to continue...")

print("You are suddenly awakened by a deafening sound.")
print(" ")
press_enter_to_continue()
print("It seems as though half the plane is missing. Wind roars into the cabin as you can see the sky through what use to be the hull of the plane.")
print(" ")
print("Where is everybody? all the seats are empty. You feel almost weightless as the plane descends uncontrollably.")
print(" ")
press_enter_to_continue()

# pre-crash choice for player

print("*PLAYER CHOICE: Do you want to BUCKLE your seatbelt or attempt to make it to the COCKPIT? (buckle/cockpit)")

crashChoice = input("> ")

if (crashChoice.lower().strip() == "buckle"):
    print("You try to latch the buckle, but one half is missing. It looks like half the belt was torn off the seat by something.")
    print("You look out of the mangled hull and see trees and ground rapidly approaching.")
    press_enter_to_continue()

elif (crashChoice.lower().strip() == "cockpit"):
    print("You make your way to the cockpit. The door is ajar so you push it open. There is nobody inside, but both seats are covered in blood.")
    print("You look out of the cockpit window and see trees and ground rapidly approaching.")
    press_enter_to_continue()
else:
    print("Please choose (buckle) or (cockpit)")

# crash narrative

print("-----")
print("You hear the sound of metal being crushed and tree branches snapping before everything goes black.")
time.sleep(2)
print("-----")
print("An image of passengers screaming on the plane goes through your mind.")
time.sleep(1)
print("-----")
print("You see a man in a blue plaid shirt pull a pistol while yelling. Blood sprays across the window behind him and he goes silent.")
time.sleep(1)
print("-----")
print("Everything goes black again...")
time.sleep(2)
press_enter_to_continue()
print("-----")
print("Your eyes open, and the real world surrounds you once again. You look around to find yourself laying inside the crashed plane.")
print("-----")
print("There is glass and jagged metal everywhere. Masks still dangle from above several seats, and you can see an overturned cart that once held snacks and liquor")
print("You look outside and see dense forest.")

## Start of decision making for player

print("*PLAYER CHOICE: Do you want to LEAVE or EXPLORE the plane? (leave/explore)")

wakeUpChoice = input("> ")

if (wakeUpChoice.lower().strip() == "leave"):
    print("You make your way out of the mangled wreckage. The wreckage looks more like a torn up tin can than an airplane.")
    print("Dense forest surrounds you in all directions.")
    press_enter_to_continue()

elif (wakeUpChoice.lower().strip() == "explore"):
    print("There is not much to explore, as the wreckage is barely recognizable as having ever been an airplane")
    print("You see a seat that appears to still be intact, and the overturned snack cart.")
    press_enter_to_continue()
    print("*PLAYERCHOICE: Do you want to explore the SEAT or the CART? (seat/cart)")
    planeChoice = input("> ")
    if (planeChoice.lower().strip() == "seat"):
        print("As you approach the seat, you can see from behind that someone still appears to be sitting in it")
        press_enter_to_continue()
        print("You walk around to the front of the seat, and a woman dressed in a stewardess outfit is still strapped in")
        print("-----")
        print("Her face is frozen in fear, almost as if she's still alive and sees something terrifying.")
        print("But her eyes won't blink, and the contorted look of her jaw is so unnatural that there is no question as to her status among the dead.")
        print("*PLAYERCHOICE: Do you want to explore the cart? (yes/no)")
        planeChoice2 = input("> ")
        if (planeChoice2.lower().strip() == "yes"):
            print("Nothing but a mini bottle of Fireball whiskey. Mmmm, smooth.")
            press_enter_to_continue()
        else:
            print("You make your way out of the mangled wreckage. The wreckage looks more like a torn up tin can than an airplane.")
            print("Dense forest surrounds you in all directions.")
            press_enter_to_continue()
    elif (planeChoice.lower().strip() == "cart"):
        print("Nothing but a mini bottle of Fireball whiskey. Mmmm, smooth.")
        press_enter_to_continue()
        print("*PLAYERCHOICE: Do you want to explore the seat? (yes/no)")
        planeChoice3 = input("> ")
        if (planeChoice3.lower().strip() == "yes"):
            print("As you approach the seat, you can see from behind that someone still appears to be sitting in it")
            press_enter_to_continue()
            print("You walk around to the front of the seat, and a woman dressed in a stewardess outfit is still strapped in")
            print("-----")
            print("Her face is frozen in fear, almost as if she's still alive and sees something terrifying.")
            print("But her eyes won't blink, and the contorted look of her jaw is so unnatural that there is no question as to her status among the dead.")
        else:
            print("You make your way out of the mangled wreckage. The wreckage looks more like a torn up tin can than an airplane.")
            print("Dense forest surrounds you in all directions.")
            press_enter_to_continue()


else:
    print("Please choose (leave) or (explore)")




