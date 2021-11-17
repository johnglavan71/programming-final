from Player import p
from Randomizer import *

class items:
    # type is the class you choose
    def __init__(self,name, hp, dfn, atk):
        self.name = name
        self.hp = hp
        self.dfn = dfn
        self.atk = atk

#forest
#from yggdrasil
def boat1():
    nameme = 'Boat'
    hp = 0
    dfn = 0
    atk = 0
    boat = items(nameme, hp, dfn, atk)
    return boat
boat = boat1()

#from maze
def medhead():#oshdfiushdafiwuicsahiueyhcryfcbywubcfysudhaiudhiuahfioa
    nameme = 'Medusas Head'
    hp = 0
    dfn = 5
    atk = 5
    mhead = items(nameme, hp, dfn, atk)
    return mhead
mhead=medhead()


#ocean
#magic conch
def m_c():
    nameme = 'Magic Conch'
    hp = 10
    dfn = 0
    atk = 0
    mc = items(nameme, hp, dfn, atk)
    return mc
mc = m_c()

#pirate hat that comes from the
def phat():#koishofgiuhsoiufhosihfoishgoishgioesn
    nameme = 'Pirates Hat'
    hp = 0
    dfn = ran110
    atk = ran1020
    pihat = items(nameme, hp, dfn, atk)
    return pihat
pihat = phat()

#Shark Fin
def Sharkfin():#BJSOIUHFIHOIFDHSAOIUHFOIUSHFSIUHFIOSUHFOSIUHSOHSOFIhoiahofiaoih
    nameme = 'Sharks Fin'
    hp = 10
    dfn = 10
    atk = 0
    sharkfin = items(nameme, hp, dfn, atk)
    return sharkfin
sfin = Sharkfin()


#marsh
#Generic item from the mych randomized
def gweapon():#sehdifhcifibhsufgcsuyfsiuyfiushfoiushgoihsoiughsoihgsoihgosih
    nameme = '(Generic Weapon)'
    hp = ran110
    dfn = 0
    atk = ran1020
    gw = items(nameme, hp, dfn, atk)
    return gw
gw = gweapon()

#key to hell
def kth():
    nameme = 'The Key to Hell'
    hp = 0
    dfn = 0
    atk = 0
    key = items(nameme, hp, dfn, atk)
    return key
key = kth()

#Generic accesory randomized`
def genacc():
    nameme = '(Generic Accesory)'
    hp = ran15
    dfn = ran110
    atk = 0
    ga = items(nameme, hp, dfn, atk)
    return ga
ga = genacc()

#castle
#From cv
def food():
    nameme = 'Bread'
    hp = ran15
    dfn = 0
    atk = 0
    Bread = items(nameme, hp, dfn, atk)
    return Bread
bread = food()

#hades crab lol
def wcrab():
    nameme = "Weasel's Pissed Off Friend"
    hp = (0-1000000)
    dfn = (0-1000000)
    atk = (0-1000000)
    hc = items(nameme, hp, dfn, atk)
    return hc
hc = wcrab()

def wcrab2():
    nameme = "Weasel's Super Friend"
    hp = ran1001000
    dfn = ran1001000
    atk = ran1001000
    hc = items(nameme, hp, dfn, atk)
    return hc
hc = wcrab2()

#mountains
#from pp
def persbles():#siuhfihsvfichsifhsiohfciuwhsfiuchsiufhcsiuhfsiuchsdggsdg
    nameme = "Persephone's Blessing"
    hp = ran1020
    dfn = ran1020
    atk = 0
    pb = items(nameme, hp, dfn, atk)
    return pb
pb = persbles()

#from zeus
def clegs():
    nameme = 'Crab Legs'
    hp = 20
    dfn = 10
    atk = 0
    cl = items(nameme, hp, dfn, atk)
    return cl
cl = clegs()

#hell
def cerb():
    nameme = 'Cerberus'
    hp = ran120
    dfn = ran120
    atk = ran120
    dog = items(nameme, hp, dfn, atk)
    return dog
dog = cerb()

#from village
#barbarian
def club():
    nameme = 'Wooden Club'
    hp = 9
    dfn = 9
    atk = 9
    wc = items(nameme, hp, dfn, atk)
    return wc
wc = club()

#wizard
def wand():
    nameme = 'Magic Stick'
    hp = 10
    dfn = 5
    atk = 14
    stick = items(nameme, hp, dfn, atk)
    return stick
stick = wand()

#knight
def sword():
    nameme = 'Training Sword'
    hp = 9
    dfn = 19
    atk = 14
    ts = items(nameme, hp, dfn, atk)
    return ts
ts = sword()

#rogue
def dagger():
    nameme = 'Rusty Dagger'
    hp = 0
    dfn = 0
    atk = 14
    rd = items(nameme, hp, dfn, atk)
    return rd
rd = dagger()