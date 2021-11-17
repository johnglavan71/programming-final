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
# no we've committed to it now lol
# full send from here
# yeah
# i finished the descriptions what should i start on next? the actual character?
# either start with the actual characters in main code or try to start how we set up fights
# i should learn the class thing then try and crate the actual character before we create the other stuff
# lets do it like that then. When we meet up you can teach me
# sounds good. You might want to read the descriptions it might help with some ideas for dialogue.
# Will do
# I live in a constant state of fear and misery.

from time import sleep
from Player import p
from Inventory import minv
from Items import stick, ts, rd, wc
from Fights import fight1


def trader():  # place in starting village (assuming its the first NPC the player meets)
    print("\nTraveler, welcome to these graceful lands there are many adventures that await")
    sleep(1)
    print("\nI am the traveling trader looking for my way into the Castle Town to sell my goods")
    sleep(1)
    ta = input("\nWould you like to take a look at my inventory? yes or no?")
    if ta == "yes":
        print("Very well then..")
        sleep(1)
        trader_inventory()
    elif ta == "no":
        print("We'll meet at a later date goodbye for now new friend.")
        sleep(1)
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


def cetus_boss():  # boss spot in cthullu
    print("You're the traveler I've heard so much about.")
    sleep(1)
    print("These waters work in my favor, good luck in this battle..")
    #initate battle
    #if cetus wins

    #if cetus loses




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

    #if gvnh loses


def castle_trader():  # place in castle village
    print("'Traveler come check out my goods.'")
    sleep(1)
    print("'WAIT!! I know you! Looks like we both made passage to the castle!")
    sleep(1)
    cta = input("'Hope your adventures have been as well as mine. Want to take a look at my updated inventory?'\n"
          "yes or no?")
    if cta == "yes" or cta == "Yes" or cta == "YES":
        print("Very well then..")
        sleep(1)
        castle_trader_inventory()
    elif cta == "no" or cta == "No" or cta == "NO":
        print("Come back anytime old friend. Ill be here")
        sleep(1)
        cv()
    else:
        print("Seems to me like you still have that hearing problem. ")
        sleep(1)
        castle_trader()



def chasm_boss():#"Darkness" name of boss, place in mysterious chasm., spits out gold, generic item
    print("Traveler? The one I've heard about in the marsh, I know you can't see me but I'm here")
    print("I've always been here, many people call me darkness. No adventurer has ever made it past me,")
    print("you are not going to be the first")
    sleep(2)
    #iniate fight
    #if darkness wins
    #if darkness loses


def persephone():  # place in persephone's pass, john want to give this a shot at the dialogue
    print("Oh a Traveler? Ive heard rumors that there was a new traveler in these lands.")
    print("I do not wish to fight but im sure the god of this land would be mad at me if I didn't.")
    print("Dont worry for this will end quickly.")
    sleep(2)
    # iniate fight
    # if persephone wins
    print("Im sorry. I did now wish to do this to you. Rest easy I will bring you back to the village.")
    #make character go to village
    # if Persephone loses

def pirates():  # place in port
    print("Welcome to the ports adventurer, what brings you around these waters??")
    sleep(2)
    print("Not much of a talker are ya, well lets hope you're good at listening..")
    sleep(1)
    print("The castle walls have aged for thousands and thousands of years, many men have \n"
          "tried to conquor what lies within these lands")


def charon():  # place in cypruss graveyard
    print("'Hello there young man, I have heard of your travels and it seems to me you're looking for something.\n"
          "I am Charon, you can think of me as a ferryman. I can give souls a ride straight to Hades.' ")
    sleep(2.5)
    cha = input("I have here a key, a key that can bring you to a special place. Would you like me to take you?\n"
                "yes or no? : ")
    if cha == "yes" or cha == "Yes" or cha == "YES":
        print("'Very well then, follow me.......\n")
        sleep(2)
        print("\n"
              "\n"
              " to the last place you will ever see'")
        sleep(4)
        # underworld
    elif cha == "no" or cha == "No" or cha == "NO":
        sleep(1)
        print("'Very well, I am sure I'll be watching, I mean see you later..'")
    else:
        print("'BOY, DID YOU NOT HEAR ME!!!!!!'")


def cerberus():  # either use with "help" or as a guide for entering castle town differently to get to the castle
    cera = input("This dog looks lost... do you want to help him? yes or no? ")
    if cera == "yes" or cera == "Yes" or cera == "YES":
        print("'Thank you so much sir'")
        sleep(1)
        print("Woah it talks")
        sleep(1)
        print("'You're the first person to offer me help thank you, my master will be pleased to meet you.")
        sleep(1)
        cg()
    elif cera == "no" or cera == "No" or cera == "NO":
        print("'Please sir, please I need help'")
        sleep(1)
        print("GET OUT OF HERE DOG!")
        sleep(1)
        cg()
    else:
        print("Am I dreaming... I should rethink this. ")
        cerberus()


def thief():  # put in slums when swiping "random number 5-10" gold or coins from player
    print("Walking through the slums a man who you passed earlier pickpocketed you\n"
          "not knowing at all you glance around look for suspicious people.")
    thiefa = input("Is your class a rogue? yes or no? : ")
    if thiefa == "yes" or thiefa == "Yes" or thiefa == "YES":
        print("something about you chasing the man back and getting your money back")
        #this is where we add onto the whole thief situation
    elif thiefa == "no" or cera == "No" or cera == "NO":
        print("Your class is not registered to take action.")
        slums()
    else:
        print("Improper input try again...")
        sleep(2)


def boss1():  # main story boss 'the great weasel'
    print("You see a large shadow filling the wall ahead of you, you shake with fear.")
    sleep(1)
    print("Emerges, The Great Weasel from his den and you see a regular sized Weasel.")
    sleep(1)
    print("Suddenly you are less worried.")
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
    print("You enter the castles main hall.")
    sleep(1)
    print('The room is full of fire, almost like you just returned to hell.')
    sleep(1)
    print('Cerberus howls and runs to greet the man in the chair.')
    print("The man is Hades God of the Underworld")
    sleep(1)
    print('"Welcome, It must have ben a long journey here young traveler.')
    print('However, You have conquered my lands and destroyed what i have built.')
    sleep(1)
    print("Get ready! You first battle will not be against me but Cerberus will take you on.")
    sleep(1)
    # initate battle of cerb
    # if "cerb" wins
    print("Master have I done well? I didnt know this traveler was so WEAK!")
    # if "cerb" loses
    print("Rest now Cerberus for it is time for me to exact your revenge")
    #initaite battle of hades
    # if "hades" wins
    print("You cannot truly believe you can beat a GOD do you?!")
    # if "cerb" loses
    print("I see you have come farther than anyone has ever expected of you. Here take this and i will return to the underworld.")
    #give crab


def trader_inventory():
    if p.playclass == 'Mage':
        if minv.wand == 'yes':
            print('I have nothing else for you')
        else:
            print('I have something that I feel like would suit you perfectly.')
            sleep(2)
            print('Here it is!')
            print('I can sell you the',stick.name)
            print(f'It will provide you with {stick.hp} hp.')
            print(f'It gives {stick.dfn} defence.')
            print(f'The spell the wand comes with will do {stick.atk} damage.')
            buy = input('It will cost you 100 gold coins. Do you want to buy it? Y/N : ')
            if buy == 'Y' or buy == 'y':
                if p.cur < 100:
                    print('You do not have enough money for that. I suggest that you go onto your first quest.')
                    go = input('Do you want to go onto your first quest? Y/N : ')
                    if go == 'Y' or go == 'y':
                        Fights.fight1()
                        trader_inventory()
                    elif go == 'n' or go == 'N':
                        print('Then please come back later.')
                    else:
                        print('You must not have heard my right.')
                        trader_inventory()
                elif p.cur >= 100:
                    p.cur -= 100
                    minv.wand = 'yes'
                    p.hp += stick.hp
                    p.atk += stick.atk
                    p.dfn += stick.dfn
                    print(f'You now have {p.cur} gold coins.')
                    print(f'You now have {p.hp} health.')
                    print(f'You now do {p.atk} damage')
                    print(f'You now have {p.dfn} decence.')
            elif buy == 'N' or buy == 'n':
                print('Very well then. However this is all i have to offer so please have a nice day.')
            else:
                print('Not sure I understand you. Lets try this again.')
                trader_inventory()



trader_inventory()