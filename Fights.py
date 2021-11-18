from Monsters import m1,m2,m3,m4,m5,m6,m7,b1,b2,b3,b4,b5,B5,b6,b7
from Player import p
from time import sleep
from Items import *
from Randomizer import *


def fight1():
    mhp = m1.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print('The villagers send you to fight off a giant rat!')
    print(f'The rat has {mhp} hp.')
    matk = m1.atk - p.dfn
    print('Monster does', matk, 'damage.')
    patk = p.atk - m1.dfn
    print('You do', patk,'damage.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y':
        while mhp > 0:
            print(f'You attack the monster.\n You deal {patk} damage.')
            mhp -= patk
            print(f'Monster has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print('You have lost! One of the villagers take you back to their home.')
                mhp = 0
                return None

        print('You have won this battle!')
        p.cur += ran15
        print(f'You now have {p.cur} gold coins!')
        print(f'You have been returned to {p.hp} health. This will happen after every battle.')
        return p.cur


def fight2():
    mhp = m2.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {m2.type} named {m2.name}.')
    print(f'It has {mhp} hp.')
    matk = m2.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m2.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the monster.\n You deal {patk} damage.')
            mhp -= patk
            print(f'Monster has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                mhp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += ran110
        print(f'You now have {p.cur} gold coins!\n')
    elif fight == "N":
        if p.playclass == 'Rogue' or p.playclass == 'Mage':
            print("You have successfully ran away.")
        elif p.playclass == 'Barbarian':
            print('You dont want to run from a fight you must show off your muscles!')
            sleep(2)
            fight2()
        elif p.playclass == 'Knight':
            print('Your honor keeps you from running from a fight')
            sleep(2)
            fight2()
        #will probably have this in a seperate loop in the movement area or in the dialogue area.
        return p.cur

def mazef():
    mhp = b1.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {b1.type} named {b1.name}..')
    print(f'She has {mhp} hp.')
    matk = b1.atk - p.dfn
    print('She does', matk, 'damage.')
    patk = p.atk - b1.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the {b1.type}.\n You deal {patk} damage.')
            mhp -= patk
            print(f'{b1.name} has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'{b1.name} attacks.\n She deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print("You tried your best. Your beautiful soul is now mine")
                mhp = 0
                f = 'f'
                return f

        print("Arrrrggg... your much better then the others traveler... be aware of whats to come")
        p.cur += ran2575
        minv.medhead = "yes"
        print('You received', {mhead.name})
        p.hp += mhead.hp
        p.atk += mhead.atk
        p.dfn += mhead.dfn
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('The maze has closed behind you. You cant leave now.')
        mazef()


def crabf():
    mhp = m3.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {m3.type} named {m3.name}.')
    print(f'It has {mhp} hp.')
    matk = m3.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m3.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the monster.\n You deal {patk} damage.')
            mhp -= patk
            print(f'Monster has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                mhp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += 0
        minv.clegs = "yes"
        print('You received', {clegs.name})
        p.hp += clegs.hp
        p.atk += clegs.atk
        p.dfn += clegs.dfn
        sleep(1)
        print(f'You now have {p.cur} gold coins!\n')
    elif fight == "N":
        if p.playclass == 'Rogue' or p.playclass == 'Mage':
            print("You have successfully ran away.")
        elif p.playclass == 'Barbarian':
            print('You dont want to run from a fight you must show off your muscles!')
            sleep(2)
            fight2()
        elif p.playclass == 'Knight':
            print('Your honor keeps you from running from a fight')
            sleep(2)
            fight2()
        #will probably have this in a seperate loop in the movement area or in the dialogue area.
        return p.cur


def sharkf():
    mhp = m4.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {m4.type} named {m4.name}.')
    print(f'It has {mhp} hp.')
    matk = m4.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m4.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the monster.\n You deal {patk} damage.')
            mhp -= patk
            print(f'Monster has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print('You fall out of your boat and the waves wash you ashore.')
                minv.boat1 = 'no'
                mhp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += ran110
        print(f'You now have {p.cur} gold coins!\n')
    elif fight == "N":
        if p.playclass == 'Rogue' or p.playclass == 'Mage':
            print("You have successfully ran away.")
        elif p.playclass == 'Barbarian':
            print('You dont want to run from a fight you must show off your muscles!')
            sleep(2)
            fight2()
        elif p.playclass == 'Knight':
            print('Your honor keeps you from running from a fight')
            sleep(2)
            fight2()
        #will probably have this in a seperate loop in the movement area or in the dialogue area.
        return p.cur


def kobaldf():
    mhp = m5.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {m5.type} named {m5.name}.')
    print(f'It has {mhp} hp.')
    matk = m5.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m5.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the monster.\n You deal {patk} damage.')
            mhp -= patk
            print(f'Monster has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                mhp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += ran1020
        print(f'You now have {p.cur} gold coins!\n')
    elif fight == "N":
        if p.playclass == 'Rogue' or p.playclass == 'Mage':
            print("You have successfully ran away.")
        elif p.playclass == 'Barbarian':
            print('You dont want to run from a fight you must show off your muscles!')
            sleep(2)
            fight2()
        elif p.playclass == 'Knight':
            print('Your honor keeps you from running from a fight')
            sleep(2)
            fight2()
        #will probably have this in a seperate loop in the movement area or in the dialogue area.
        return p.cur


def hydraf():
    mhp = m6.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {m6.type} named {b2.name}.')
    print(f'It has {mhp} hp.')
    matk = m6.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m6.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the monster.\n You deal {patk} damage.')
            mhp -= patk
            print(f'Monster has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                mhp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += ran110
        print(f'You now have {p.cur} gold coins!\n')
    elif fight == "N":
        if p.playclass == 'Rogue' or p.playclass == 'Mage':
            print("You have successfully ran away.")
        elif p.playclass == 'Barbarian':
            print('You dont want to run from a fight you must show off your muscles!')
            sleep(2)
            fight2()
        elif p.playclass == 'Knight':
            print('Your honor keeps you from running from a fight')
            sleep(2)
            fight2()
        #will probably have this in a seperate loop in the movement area or in the dialogue area.
        return p.cur



def lizardf():
    mhp = m7.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {m7.type} named {m7.name}.')
    print(f'It has {mhp} hp.')
    matk = m7.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m7.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the monster.\n You deal {patk} damage.')
            mhp -= patk
            print(f'Monster has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                mhp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += ran1100
        print(f'You now have {p.cur} gold coins!\n')
    elif fight == "N":
        if p.playclass == 'Rogue' or p.playclass == 'Mage':
            print("You have successfully ran away.")
        elif p.playclass == 'Barbarian':
            print('You dont want to run from a fight you must show off your muscles!')
            sleep(2)
            fight2()
        elif p.playclass == 'Knight':
            print('Your honor keeps you from running from a fight')
            sleep(2)
            fight2()
        #will probably have this in a seperate loop in the movement area or in the dialogue area.
        return p.cur


def cetusf():
    mhp = b2.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {b2.type} named {b2.name}..')
    print(f'He has {b2.hp} hp.')
    matk = b2.atk - p.dfn
    print('He does', matk, 'damage.')
    patk = p.atk - b2.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the {b2.type}.\n You deal {patk} damage.')
            mhp -= patk
            print(f'{b2.name} has {b2.hp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'{b2.name} attacks.\n He deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print("These waters are my home, I know them better muhahaha")
                mhp = 0
                print('Your boat was destroyed in the fight.')
                minv.boat1 = 'no'
                f = 'f'
                return f

        print("NOOOO! How? Why? UGGHGGHGHGHGH")
        print(f'You harvested cetus\'s fin and now have {sfin.name}')
        p.cur += ran1020
        minv.Sharkfin = "yes"
        print('You received', {sfin.name})
        p.hp += sfin.hp
        p.atk += sfin.atk
        p.dfn += sfin.dfn
        sleep(2)
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('The waves keep pushing you back to him.')
        cetusf()


def genvilf():
    mhp = b3.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {b3.type} named {b3.name}..')
    print(f'It has {mhp} hp.')
    matk = b3.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - b3.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the {b3.type}.\n You deal {patk} damage.')
            mhp -= patk
            print(f'{b3.name} has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'{b3.name} attacks.\n It deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print("You were no match, have fun in the underworld traveler.")
                minv.boat1 = "no"
                print("Your boat was destroyed in the fight.")
                mhp = 0
                f = 'f'
                return f

        print("You bested me, no one has ever... done.... that...")
        minv.phat = 'yes'
        p.cur += ran2575
        print('You received', {pihat.name})
        p.hp += pihat.hp
        p.atk += pihat.atk
        p.dfn += pihat.dfn
        sleep(1)
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('The pirates keep egging you on and block your way.')
        genvilf()


def persephonef():
    mhp = b4.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {b4.type} named {b4.name}..')
    print(f'She has {mhp} hp.')
    matk = b4.atk - p.dfn
    print('She does', matk, 'damage.')
    patk = p.atk - b4.dfn
    print('You do', patk,'damage, and have', php,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the {b4.type}.\n You deal {patk} damage.')
            mhp -= patk
            print(f'{b4.name} has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'{b4.name} attacks.\n She deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print("Im sorry. I did now wish to do this to you. Rest easy I will bring you back to the village.")
                f = 'f'
                return f

        print("I do not wish to fight you anymore. It is clear that your are stronger than I am. Here take this and run.")
        p.cur += b4.cur
        minv.persbles = "yes"
        print('You received', {pb.name})
        p.hp += pb.hp
        p.atk += pb.atk
        p.dfn += pb.dfn
        sleep(1)
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('Her beauty entices you to stay.')
        persephonef()


def darknessf():
    mhp = b7.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {b7.type} named {b7.name}..')
    print(f'It has {mhp} hp.')
    matk = b7.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - b7.dfn
    print('You do', patk, 'damage, and have', php, 'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while mhp > 0:
            print(f'You attack the {b7.type}.\n You deal {patk} damage.')
            mhp -= patk
            print(f'{b7.name} has {mhp} hp left.\n')
            sleep(3)
            if mhp <= 0:
                break
            print(f'{b7.name} attacks.\n It deals {matk} damage.')
            php -= matk
            print(f'You have {php} hp left.\n')
            sleep(3)
            if php <= 0:
                print("Another traveler scared of the dark, eternal rest is your fate now..")
                f = 'f'
                return f

        print("No, no, no, no, no... This can't be happening!!! For your triumph over me you get (generic item)")
        p.cur += b7.cur
        minv.gweapon = "yes"
        print('You received', {gw.name})
        p.hp += gw.hp
        p.atk += gw.atk
        p.dfn += gw.dfn
        sleep(1)
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('You cant find your way out its too dark.')
        darknessf()

def weaself():
    mhp = b6.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {b6.type} named {b6.name}..')
    print(f'The Great Weasel has {mhp} hp.')
    matk = b6.atk - p.dfn
    print('The Great Weasel does', matk, 'damage.')
    patk = p.atk - b6.dfn
    print('You do', patk, 'damage, and have', php, 'hp.')
    print("Are you ready!?")
    sleep(5)
    print('Things are going to be different. Im sure your used to attacking first huh?')
    while mhp > 0:
        print(f'{b6.name} attacks.\n It deals {matk} damage.')
        php -= matk
        print(f'You have {php} hp left.\n')
        sleep(3)
        if php <= 0:
            print("My lord will never let me die like this, you will pay!!! He will make you pay!!!!")
            f = 'f'
            return f
        pr0int(f'You attack the {b6.type}.\n You deal {patk} damage.')
        mhp -= patk
        print(f'{b6.name} has {mhp} hp left.\n')
        sleep(3)
        if mhp <= 0:
            break
    print("'You will never take my lords land! He will live on forever!'")
    sleep(2)
    p.cur += ran1100
    if minv.clegs == 'yes':
        minv.wcrab = 'yes'
        print('You received', {wc.name})
        print('You smote me earlier so now its my turn to ruin your stats ..l..')
        p.hp += wc.hp
        p.atk += wc.atk
        p.dfn += wc.dfn
        print(f'You now have {p.hp} health.')
        print(f'You now have {p.dfn} defence.')
        print(f'You now deal {p.atk} damage.')
    else:
        minv.wcrab2 = 'yes'
        print('You received', {wc2.name})
        print('I was the crab in Sandy Shores. Thank you for sparing me!')
        p.hp += wc2.hp
        p.atk += wc2.atk
        p.dfn += wc2.dfn
        print(f'You now have {p.hp} health.')
        print(f'You now have {p.dfn} defence.')
        print(f'You now deal {p.atk} damage.')
    sleep(1)
    print(f'You now have {p.cur} gold coins!\n')
    return p.cur

def Cerbf():
    mhp = B5.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {B5.type} named {B5.name}..')
    print(f'It has {mhp} hp.')
    matk = B5.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - B5.dfn
    print('You do', patk, 'damage, and have', php, 'hp.')
    while mhp > 0:
        print(f'{B5.name} attacks.\n It deals {matk} damage.')
        php -= matk
        print(f'You have {php} hp left.\n')
        sleep(3)
        if php <= 0:
            print("Master have I done well? I didnt know this traveler was so WEAK!")
            f = 'f'
            return f
        print(f'{B5.name} attacks.\n It deals {matk} damage.')
        php -= matk
        print(f'You have {php} hp left.\n')
        sleep(3)
        if php <= 0:
            print("Master have I done well? I didnt know this traveler was so WEAK!")
            f = 'f'
            return f
        print(f'{B5.name} attacks.\n It deals {matk} damage.')
        php -= matk
        print(f'You have {php} hp left.\n')
        sleep(3)
        if php <= 0:
            print("Master have I done well? I didnt know this traveler was so WEAK!")
            f = 'f'
            return f
        print(f'You attack the {B5.type}.\n You deal {patk} damage.')
        mhp -= patk
        print(f'{B5.name} has {mhp} hp left.\n')
        sleep(3)
        if mhp <= 0:
            break
    print("Rest now Cerberus for it is time for me to exact your revenge")
    Hadesf()
    return p.cur


def Hadesf():
    mhp = b5.hp
    php = p.hp
    print(f'You have {p.hp} health.')
    print(f'You run into a {b5.type} named {b5.name}..')
    print(f'It has {mhp} hp.')
    matk = b5.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - b5.dfn
    print('You do', patk, 'damage, and have', php, 'hp.')
    while mhp > 0:
        print(f'{b5.name} attacks.\n It deals {matk} damage.')
        php -= matk
        print(f'You have {php} hp left.\n')
        sleep(3)
        if php <= 0:
            print("You cannot truly believe you can beat a GOD do you?!")
            f = 'f'
            return f
        print(f'You attack the {b5.type}.\n You deal {patk} damage.')
        mhp -= patk
        print(f'{b5.name} has {mhp} hp left.\n')
        sleep(3)
        if mhp <= 0:
            break
    print("I see you have come farther than anyone has ever expected of you. Here take this and i will return to the underworld.")
    print('Congrats You BEAT the game!!!!!! WOO Hope we wasted your time with the weasel!')
    sleep(60)
    print('Oh Your still here. Well i guess ill make all of your stats maxed out.')
    p.hp = 1000000000000
    p.atk = 1000000000000
    p.dfn = 1000000000000
    print('Sorry for the wait your stats have been changed.')

    return p.cur



