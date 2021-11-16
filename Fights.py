from Monsters import m1,m2,bs
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
            print(f'The monster attacks.\n It deals {matk} damage.\n')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! One of the villagers take you back to their home.')
                m1.hp = 0
                return None
            elif m1.hp <= 0:
                break
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
            print(f'The monster attacks.\n It deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! When one of the villagers goes out for a walk they find you asleep in the woods.')
                m2.hp = 0
                f = 'f'
                return f
            elif m2.hp <= 0:
                break
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
            print(f'{b1.name} attacks.\n She deals {matk} damage.')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print("You tried your best. Your beautiful soul is now mine")
                b1.hp = 0
                f = 'f'
                return f
            elif b1.hp <= 0:
                break
        print("Arrrrggg... your much better then the others traveler... be aware of whats to come")
        p.cur += b1.cur
        print(f'You now have {p.cur} gold coins!\n')
    elif fight == "N":
        print('The maze has closed behind you. You cant leave now.')
        #will probably have this in a seperate loop in the movement area or in the dialogue area.
        return p.cur

