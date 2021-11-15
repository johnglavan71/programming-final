class items:
    # type is the class you choose
    def __init__(self,name, hp, dfn, atk):
        self.name = name
        self.hp = hp
        self.dfn = dfn
        self.atk = atk

#forest
#from yggdrasil
def boat():
    nameme = 'Boat'
    hp = 0
    dfn = 0
    atk = 0
    boat = items(nameme, hp, dfn, atk)
    return boat

#from maze
def mhead():
    nameme = 'Medusas Head'
    hp = 0
    dfn = 20
    atk = 0
    mhead = items(nameme, hp, dfn, atk)
    print(mhead.name)
    print(mhead.name,'gives you',mhead.dfn, 'defence.')
    return mhead


#ocean
#magic conch
def m_c():
    nameme = 'Magic Conch'
    hp = 0
    dfn = 0
    atk = 0
    m_c = items(nameme, hp, dfn, atk)
    return m_c

#pirate hat that comes from the
def phat():
    nameme = 'Pirates Hat'
    hp = 0
    dfn = 0
    atk = 0
    pihat = items(nameme, hp, dfn, atk)
    return pihat

#Shark Fin
def Sharkfin():
    nameme = 'Sharks Fin'
    hp = 0
    dfn = 0
    atk = 0
    sharkfin = items(nameme, hp, dfn, atk)
    return sharkfin


#marsh
#Generic item from the mych randomized
def gweapon():
    nameme = '(Generic Weapon)'
    hp = 0
    dfn = 0
    atk = 0
    gw = items(nameme, hp, dfn, atk)
    return gw

#key to hell
def kth():
    nameme = 'The Key to Hell'
    hp = 0
    dfn = 0
    atk = 0
    key = items(nameme, hp, dfn, atk)
    return key

#Generic accesory randomized`
def genacc():
    nameme = '(Generic Accesory)'
    hp = 0
    dfn = 0
    atk = 0
    ga = items(nameme, hp, dfn, atk)
    return ga

#castle
#From cv
def food():
    nameme = 'Bread'
    hp = 0
    dfn = 0
    atk = 0
    Bread = items(nameme, hp, dfn, atk)
    return Bread

#hades crab lol
def hcrab():
    nameme = "Hade's Crab"
    hp = 0
    dfn = 0
    atk = 0
    hc = items(nameme, hp, dfn, atk)
    return hc

#mountains
#from pp
def persbles():
    nameme = "Persephone's Blessing"
    hp = 0
    dfn = 0
    atk = 0
    pb = items(nameme, hp, dfn, atk)
    return pb

#from zeus
def Lbolt():
    nameme = 'Lightning Bolt'
    hp = 0
    dfn = 0
    atk = 0
    lb = items(nameme, hp, dfn, atk)
    return lb

#boss
def lores():
    nameme = 'Lore'
    hp = 0
    dfn = 0
    atk = 0
    lore = items(nameme, hp, dfn, atk)
    return lore


#hell
def cerb():
    nameme = 'Cerberus'
    hp = 0
    dfn = 0
    atk = 0
    dog = items(nameme, hp, dfn, atk)
    return dog

#from village
#barbarian
def club():
    nameme = 'Wooden Club'
    hp = 0
    dfn = 0
    atk = 0
    wc = items(nameme, hp, dfn, atk)
    return wc

#wizard
def wand():
    nameme = 'Magic Stick'
    hp = 0
    dfn = 0
    atk = 0
    stick = items(nameme, hp, dfn, atk)
    return stick

#knight
def sword():
    nameme = 'Training Sword'
    hp = 0
    dfn = 0
    atk = 0
    ts = items(nameme, hp, dfn, atk)
    return ts

#rogue
def dagger():
    nameme = 'Rusty Dagger'
    hp = 0
    dfn = 0
    atk = 0
    rd = items(nameme, hp, dfn, atk)
    return rd

mhead()