from Monsters import m1,m2,m3,m4,m5,m6,m7,b1,b2,b3,b4,b5,B5,b6,b7
from Player import p
from time import sleep


def fight1():
    print('The villagers send you to fight off a giant rat!')
    print(f'The rat has {m1.hp} hp.')
    matk = m1.atk - p.dfn
    print('Monster does', matk, 'damage.')
    patk = p.atk - m1.dfn
    print('You do', patk,'damage.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y':
        while m1.hp > 0:
            print(f'\nYou attack the monster.\n You deal {patk} damage.\n')
            m1.hp -= patk
            print(f'Monster has {m1.hp} hp left.\n')
            sleep(2)
            if m1.hp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.\n')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! One of the villagers take you back to their home.')
                m1.hp = 0
                return None

        print('You have won this battle!')
        p.cur += m1.cur
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur

def fight2():
    print(f'You run into a {m2.type} named {b2.name}.')
    print(f'It has {m2.hp} hp.')
    matk = m2.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m2.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while m2.hp > 0:
            print(f'\nYou attack the monster.\n You deal {patk} damage.\n')
            m2.hp -= patk
            print(f'Monster has {m2.hp} hp left.')
            sleep(2)
            if m2.hp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                m2.hp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += m2.cur
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
    print(f'You run into a {b1.type} named {b1.name}..')
    print(f'She has {b1.hp} hp.')
    matk = b1.atk - p.dfn
    print('She does', matk, 'damage.')
    patk = p.atk - b1.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while b1.hp > 0:
            print(f'\nYou attack the {b1.type}.\n You deal {patk} damage.\n')
            b1.hp -= patk
            print(f'{b1.name} has {b1.hp} hp left.')
            sleep(2)
            if b1.hp <= 0:
                break
            print(f'{b1.name} attacks.\n She deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print("You tried your best. Your beautiful soul is now mine")
                b1.hp = 0
                f = 'f'
                return f

        print("Arrrrggg... your much better then the others traveler... be aware of whats to come")
        p.cur += b1.cur
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('The maze has closed behind you. You cant leave now.')
        mazef()


def crabf():
    print(f'You run into a {m3.type} named {b2.name}.')
    print(f'It has {m3.hp} hp.')
    matk = m3.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m3.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while m3.hp > 0:
            print(f'\nYou attack the monster.\n You deal {patk} damage.\n')
            m3.hp -= patk
            print(f'Monster has {m3.hp} hp left.')
            sleep(2)
            if m3.hp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                m3.hp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += m3.cur
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
    print(f'You run into a {m4.type} named {b2.name}.')
    print(f'It has {m4.hp} hp.')
    matk = m4.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m4.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while m4.hp > 0:
            print(f'\nYou attack the monster.\n You deal {patk} damage.\n')
            m4.hp -= patk
            print(f'Monster has {m4.hp} hp left.')
            sleep(2)
            if m4.hp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                m4.hp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += m4.cur
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
    print(f'You run into a {m5.type} named {b2.name}.')
    print(f'It has {m5.hp} hp.')
    matk = m5.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m5.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while m5.hp > 0:
            print(f'\nYou attack the monster.\n You deal {patk} damage.\n')
            m5.hp -= patk
            print(f'Monster has {m5.hp} hp left.')
            sleep(2)
            if m5.hp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                m5.hp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += m5.cur
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
    print(f'You run into a {m6.type} named {b2.name}.')
    print(f'It has {m6.hp} hp.')
    matk = m6.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m6.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while m6.hp > 0:
            print(f'\nYou attack the monster.\n You deal {patk} damage.\n')
            m6.hp -= patk
            print(f'Monster has {m6.hp} hp left.')
            sleep(2)
            if m6.hp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                m6.hp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += m6.cur
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
    print(f'You run into a {m7.type} named {m7.name}.')
    print(f'It has {m7.hp} hp.')
    matk = m7.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - m7.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while m7.hp > 0:
            print(f'\nYou attack the monster.\n You deal {patk} damage.\n')
            m7.hp -= patk
            print(f'Monster has {m7.hp} hp left.')
            sleep(2)
            if m7.hp <= 0:
                break
            print(f'The monster attacks.\n It deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                m7.hp = 0
                f = 'f'
                return f

        print('You have won this battle!')
        p.cur += m7.cur
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
    print(f'You run into a {b2.type} named {b2.name}..')
    print(f'He has {b2.hp} hp.')
    matk = b2.atk - p.dfn
    print('He does', matk, 'damage.')
    patk = p.atk - b2.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while b2.hp > 0:
            print(f'\nYou attack the {b2.type}.\n You deal {patk} damage.\n')
            b2.hp -= patk
            print(f'{b2.name} has {b2.hp} hp left.')
            sleep(2)
            if b2.hp <= 0:
                break
            print(f'{b2.name} attacks.\n He deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print("These waters are my home, I know them better muhahaha")
                b2.hp = 0
                f = 'f'
                return f

        print("NOOOO! How? Why? UGGHGGHGHGHGH")
        p.cur += b2.cur
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('The waves keep pushing you back to him.')
        cetusf()


def genvilf():
    print(f'You run into a {b3.type} named {b3.name}..')
    print(f'It has {b3.hp} hp.')
    matk = b3.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - b3.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while b3.hp > 0:
            print(f'\nYou attack the {b3.type}.\n You deal {patk} damage.\n')
            b3.hp -= patk
            print(f'{b3.name} has {b3.hp} hp left.')
            sleep(2)
            if b3.hp <= 0:
                break
            print(f'{b3.name} attacks.\n It deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print("You were no match, have fun in the underworld traveler.")
                b3.hp = 0
                f = 'f'
                return f

        print("You bested me, no one has ever... done.... that...")
        p.cur += b3.cur
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('The pirates keep egging you on and block your way.')
        genvilf()


def persephonef():
    print(f'You run into a {b4.type} named {b4.name}..')
    print(f'She has {b4.hp} hp.')
    matk = b4.atk - p.dfn
    print('She does', matk, 'damage.')
    patk = p.atk - b4.dfn
    print('You do', patk,'damage, and have', p.hp,'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while b4.hp > 0:
            print(f'\nYou attack the {b4.type}.\n You deal {patk} damage.\n')
            b4.hp -= patk
            print(f'{b4.name} has {b4.hp} hp left.')
            sleep(2)
            if b4.hp <= 0:
                break
            print(f'{b4.name} attacks.\n She deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print("Im sorry. I did now wish to do this to you. Rest easy I will bring you back to the village.")
                f = 'f'
                return f

        print("I do not wish to fight you anymore. It is clear that your are stronger than I am. Here take this and run.")
        p.cur += b4.cur
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('Her beauty entices you to stay.')
        persephonef()


def darknessf():
    print(f'You run into a {b7.type} named {b7.name}..')
    print(f'It has {b7.hp} hp.')
    matk = b7.atk - p.dfn
    print('It does', matk, 'damage.')
    patk = p.atk - b7.dfn
    print('You do', patk, 'damage, and have', p.hp, 'hp.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y' or fight == 'y':
        while b7.hp > 0:
            print(f'\nYou attack the {b7.type}.\n You deal {patk} damage.\n')
            b7.hp -= patk
            print(f'{b7.name} has {b7.hp} hp left.')
            sleep(2)
            if b7.hp <= 0:
                break
            print(f'{b7.name} attacks.\n It deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print("Another traveler scared of the dark, eternal rest is your fate now..")
                f = 'f'
                return f

        print("No, no, no, no, no... This can't be happening!!! For your triumph over me you get (generic item)")
        p.cur += b7.cur
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur
    elif fight == "N":
        print('You cant find your way out its too dark.')
        darknessf()


