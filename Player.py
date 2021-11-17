#want to double check the characters tab just to see if im doing it correctly

class player:
    # type is the class you choose
    def __init__(self, name, playclass, hp, dfn, atk, cur, bsmith):
        self.name = name
        self.playclass = playclass
        self.hp = hp
        self.dfn = dfn
        self.atk = atk
        self.cur = cur
        self.bsmith = bsmith
nameme = input('What is your name? : ')
def retry():
    classc()

def classc():
    classchoice = 0
    while classchoice != 'Mage' or classchoice != 'Barbarian' or classchoice != 'Knight' or classchoice!= 'Rogue':
        classchoice = input('Please choose your class.\n'
                            'Mage : Uses magic to slay your foes in mysterious ways.\n'
                            'Barbarian : All you know is how to fight.\n'
                            'Knight : You MUST protect the others.\n'
                            'Rogue : Stealth and steal is what your best at.\n'
                            ':')
        if classchoice == 'Mage' or classchoice == 'Barbarian' or classchoice == 'Knight' or classchoice== 'Rogue' or classchoice == 'admin':
            break

    if classchoice == 'Mage':
        hp = 10
        dfn = 0
        atk = 1
        cur = 5
        bsmith = 1
        p = player(nameme, classchoice, hp, dfn, atk, cur, bsmith)
    elif classchoice == 'Barbarian':
        hp = 10
        dfn = 0
        atk = 150
        cur = 100
        bsmith = 1
        p = player(nameme, classchoice, hp, dfn, atk, cur, bsmith)
    elif classchoice == 'Knight':
        hp = 100
        dfn = 50
        atk = 125
        cur = 100
        bsmith = 1
        p = player(nameme, classchoice, hp, dfn, atk, cur, bsmith)
    elif classchoice == 'Rogue':
        hp = 10
        dfn = 10
        atk = 100
        cur = 100
        bsmith = 1
        p = player(nameme, classchoice, hp, dfn, atk, cur, bsmith)
    elif classchoice == 'admin':
        playclass = Mage
        hp = 1000000000
        dfn = 100000000
        atk = 100000000
        cur = 100000000
        bsmith = 0
        p = player(nameme, playclass, hp, dfn,atk,cur,bsmith)


    return p


p = classc()
print(f'Your name is {p.name}.')
print(f'Your class is {p.playclass}.')
print(f'You have {p.hp} health points.')
print(f'You do {p.atk} damage.')
print(f'You block {p.dfn} damage.')
print(f'You have {p.cur} gold coins.\n')


