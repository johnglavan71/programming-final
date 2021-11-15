# ta = trader answer
# ba = blacksmith answer
# ya = yggrasil answer (until we find a new name)
# mba(until we find a new name) = maze boss answer
# ca = cetus answer
# gnvha = generic_villian_name_here answer
# cta = castle trader answer
# pa = persephone answer
# pia(dont want to copy perspephony answer) = pirates answer
# cha = charon answer
# cera = cerberus answer
# thiefa = thief answer
# boss1a = boss1 answer
# hadesa = hades answer


# why did we create so many characters?!?!?!
# we can always chop it down a bit
# no weve committed to it now lol
# full send from here
# yeah
# i finnished the descriptions what should i start on next? the actuall character?
# either start with the actual characters in main code or try to start how we set up fights
# i should learn the class thing then try and crate the actual character before we create the other stuff
# lets do it like that then. When we meet up you can teach me
# sounds good. You might want to read the descriptions it might help with some ideas for dialogue.
# Will do
# I live in a constant state of fear and misery.

from time import sleep


def trader():  # place in starting village (assuming its the first NPC the player meets)
    print("Traveler, welcome to these graceful lands there are many adventures that await")
    sleep(1)
    print("I am the traveling trader looking for my way into the Castle Town to sell my goods")
    sleep(1)
    ta = input("Would you like to take a look at my inventory? yes or no?")
    if ta == "yes":
        print("Very well then..")
        sleep(1)
        trader_inventory()
    elif ta == "no":
        print("We'll meet at a later date goodbye for now new friend.")
        sleep(1)
        village()
    else:
        print("Seems to me like you did not understand me at all... ")
        sleep(1)
        trader()


def blacksmith():  # place in starting village after trader dialogue
    print("Hello there traveler, I am this small village's blacksmith.")
    sleep(1)
    print("I supply weapon and armor upgrades for all of the land.")
    sleep(1)
    ba = input("Would you like to take a gander at my forged goods? yes or no : ")
    if ba == "yes":
        print("You wont be dissapointed!")
        sleep(1)
        blacksmith_inventory()
    elif ba == "no":
        print("Farewell traveler")
        sleep(1)
        village()
    else:
        print("For goodness sakes are you deaf, I guess I'll repeat myself..")
        blacksmith()


def yggdrasil():  # Make it sound like an old wise man telling stories about past travelers.sir yes sir
    print("Ohhh look here, another traveler come to save the lands like the others?")
    sleep(1)
    print("I've seen many travelers like you move through these parts in search of justice, you look kind maybe i can help you out")
    sleep(1)
    print("Here is a token for your kindness, to help you sail these treterous waters")
    # gives boat on this line idk the command
    sleep(1)


def maze_boss():  # we need to find name for boss. Make it a gorgon... totally not what medusa is... LOREEEEEEE! WE STICK TO LORE HERE
    print("You navigate a maze well, good luck defeating me")
    # initate battle
    # if 'gorgon' won
    print("you tried your best your beautiful soul is now mine")
    # if 'gorgon' loses
    print("arrrrggg... your much better then the others traveler... be aware of whats to come")


def Cetus_boss():  # boss spot in cthullu
    print("You're the traveler I've heard so much about.")
    sleep(1)
    print("These waters work in my favor, good luck in this battle..")
    #initate battle
    #if cetus wins
    print("These waters are my home, I know them better muhahaha")
    #if cetus loses
    print("NOOOO! How? Why? UGGHGGHGHGHGH")



def generic_villian_name_here():  # boss spot in forbidden seas, evil pirate
    print("Through the thick fog you see a man emerging from the cloudy horizon")
    sleep(1)
    print("I've heard about your adventures young man.")
    sleep(1)
    print("But have you heard of me, you traveled into my domain, I am the (enter 'Enter generic villan name here').")
    sleep(1)
    print("NO MORE TALKING WE FIGHT NOW!!!!!")
    sleep(1)
    #initate fight
    #if gvnh wins
    print("You were no match, have fun in the underworld traveler.")
    #if gvnh loses
    print("You bested me, no one has ever... done.... that...")


def castle_trader():  # place in castle village



def chasm_boss():#"Darkness" name of boss, place in mysterious chasm., spits out gold, generic item
    print("Traveler? The one I've heard about in the marsh, I know you can't see me but I'm here")
    print("I've always been here, many people call me darkness. No adventurer has ever made it past me,")
    print("you are not going to be the first")
    sleep(2)
    #iniate fight
    #if darkness wins
    print("Another traveler scared of the dark, eternal rest is your fate now..")
    #if darkness loses
    print("No, no, no, no, no... This can't be happening!!! For your triumph over me you get (generic item)")


def persephone():  # place in persephone's pass, john want to give this a shot at the dialogue


def pirates():  # place in port
    print("Welcome to the ports adventurer, what brings you around these waters??")
    sleep(2)
    print("Not much of a talker are ya, well lets hope you're good at listening..")
    sleep(1)
    print("The castle walls have aged for thousands and thousands of years, many men have \n"
          "tried to conquor what lies within these lands")


def charon():  # place in cypruss graveyard


def cerberus():  # either use with "help" or as a guide for entering castle town differently to get to the castle
    cera = input("This dog looks lost... do you want to help him? yes or no? ")
    if cera == "yes" or cera == "Yes" or cera == "YES":
        print("'Thank you so much sir'")
        sleep(1)
        print("Woah it talks")
        sleep(1)
        print


def thief():  # put in slums when swiping "random number 5-10" gold or coins from player


def boss1():  # main story boss 'the great weasel'
    print("You see a large shadow filling the wall ahead of you, you shake with fear.")
    print("Emerges, The Great Weasel from his den.")
    sleep(1)
    print('"Welcome traveler, I see you have almost taken over this whole land. I am The Great Weasel,')
    print(' my lords great protector. I will not let you take his land!"')
    sleep(1)
    print("you raise your weapon and ready for battle")
    sleep(1)
    #initate battle
    #if "TGW" wins
    print("'You will never take my lords land! He will live on forever!'")
    #if "TGW" loses
    print("My lord will never let me die like this, you will pay!!! He will make you pay!!!!")


def hades():  # EE boss John write your characters dialog you know it best
