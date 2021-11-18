

class monster:
    # type is the class you choose
    def __init__(self, name, type, hp, dfn, atk, cur):
        self.name = name
        self.type = type
        self.hp = hp
        self.dfn = dfn
        self.atk = atk
        self.cur = cur

def villagemonster():
    name = 'The Fat Rat'
    type = 'Rat'
    hp = 5
    dfn = 0
    atk = 1
    cur =1
    m1 = monster(name, type, hp, dfn, atk, cur)
    return m1
m1 = villagemonster()


def forsetmonster():
    name = 'Lykaion'
    type = 'Wolf'
    hp = 25
    dfn = 5
    atk = 5
    cur = 15
    m2 = monster(name, type, hp, dfn, atk, cur)
    return m2
m2 = forsetmonster()


def ssmonster():
    name = 'Happy Crab'
    type = 'Crab'
    hp = 1000
    dfn = 0
    atk = 0
    cur = 0
    m3 = monster(name, type, hp, dfn, atk, cur)
    return m3
m3 = ssmonster()


def ddmonster():
    name = 'Akheilos'
    type = 'Shark'
    hp = 60
    dfn = 10
    atk = 25
    cur = 50
    m4 = monster(name, type, hp, dfn, atk, cur)
    return m4
m4 = ddmonster()


def ironmonster():
    name = 'Talos'
    type = 'Kobald'
    hp = 75
    dfn = 20
    atk = 30
    cur = 100
    m5 = monster(name, type, hp, dfn, atk, cur)
    return m5
m5 = ironmonster()


def mmmonster():
    name = 'Lernaean'
    type = 'Hydra'
    hp = 25
    dfn = 5
    atk = 15
    cur = 20
    m6 = monster(name, type, hp, dfn, atk, cur)
    return m6
m6 = mmmonster()


def gbmonster():
    name = 'Lizard man of Scape Ore Swamp'
    type = 'Lizard Man'
    hp = 100
    dfn = 15
    atk = 25
    cur = 75
    m7 = monster(name, type, hp, dfn, atk, cur)
    return m7
m7 = gbmonster()


def mazeboss():
    name= 'Medusa'
    type= 'Gorgon'
    hp= 200
    dfn= 20
    atk= 35
    cur= 1
    b1 = monster(name, type, hp, dfn, atk, cur)
    return b1
b1 = mazeboss()


def cetusboss():
    name= 'Cetus'
    type= 'Big Ass God Damn Whale'
    hp= 300
    dfn= 25
    atk= 45
    cur= 20
    b2 = monster(name, type, hp, dfn, atk, cur)
    return b2
b2 = cetusboss()


def genvillan():
    name= 'Unknown'
    type= 'Unknown'
    hp = 400
    dfn = 10
    atk = 25
    cur = 0
    b3 = monster(name, type, hp, dfn, atk, cur)
    return b3
b3 = genvillan()


def persephoneboss():
    name= 'Persephone'
    type= 'Goddess'
    hp= 600
    dfn= 5
    atk= 40
    cur= 0
    b4 = monster(name, type, hp, dfn, atk, cur)
    return b4
b4 = persephoneboss()


def cerb():
    name= 'Cerberus'
    type= '3 Headed Doge'
    hp= 3000
    dfn= 200
    atk= 20
    cur= 0
    B5 = monster(name, type, hp, dfn, atk, cur)
    return B5
B5 = cerb()


def hades():
    name= 'Hades'
    type= 'God of the Underworld'
    hp= 5000
    dfn= 50
    atk= 50
    cur= 1
    b5 = monster(name, type, hp, dfn, atk, cur)
    return b5
b5 = hades()


def thegreatweasel():
    name= 'The Great Weasel'
    type= 'Regular Sized Weasel'
    hp= 1000
    dfn= 25
    atk= 50
    cur= 1
    b6 = monster(name, type, hp, dfn, atk, cur)
    return b6
b6 = thegreatweasel()


def mcboss():
    name= '?'
    type= '?'
    hp= 1
    dfn= 1
    atk= 1
    cur= 1
    b7 = monster(name, type, hp, dfn, atk, cur)
    return b7
b7 = mcboss()