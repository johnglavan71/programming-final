from Monsters import m1,m2,m3
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
            elif m1.hp <= 0:
                break
        print('You have won this battle!')
        p.cur += m1.cur
        print(f'You now have {p.cur} gold coins!\n')
        return p.cur

def fight2():
    matk = m2.atk - p.dfn
    print('Monster does', matk, 'damage.')
    patk = p.atk - m2.dfn
    print('You do', patk,'damage.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y':
        while m2.hp > 0:
            print(f'\nYou attack the monster.\n You deal {patk} damage.\n')
            m2.hp -= patk
            print(f'Monster has {m2.hp} hp left.\n')
            sleep(2)
            print(f'The monster attacks.\n It deals {matk} damage.\n')
            p.hp -= matk
            print(f'You have {p.hp} hp left.')
            if p.hp <= 0:
                print('You have lost! One of the villagers take you back to their home.')
                m2.hp = 0
            elif m2.hp <= 0:
                break
        print('You have won this battle!')
        p.cur += m2.cur
        print(f'You now have {p.cur} gold coins!\n')
    elif fight == "N":
        print('You run back the way you came!')
        #will probably have this in a seperate loop in the movement area or in the dialogue area.
        return p.cur