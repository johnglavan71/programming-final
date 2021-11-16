from Monsters import m1
from Player import p
from time import sleep


def fight1():
    matk = m1.atk - p.dfn
    print('Monster does', matk, 'damage.')
    patk = p.atk - m1.dfn
    print('You do', patk,'damage.')
    fight = input('Do you wish to fight? Y/N \n: ')
    if fight == 'Y':
        while m1.hp > 0:
            print(f'You attack the monster.\n You deal {patk} damage.')
            m1.hp -= patk
            print(f'Monster has {m1.hp} hp left.')
            sleep(1)


fight1()