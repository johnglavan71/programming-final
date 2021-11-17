from Player import p
import Randomizer

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
    dfn = 20
    atk = 0
    mhead = items(nameme, hp, dfn, atk)
    return mhead
mhead=medhead()


#ocean
#magic conch
def m_c():
    nameme = 'Magic Conch'
    hp = 0
    dfn = 0
    atk = 0
    mc = items(nameme, hp, dfn, atk)
    return mc
mc = m_c()

#pirate hat that comes from the
def phat():#koishofgiuhsoiufhosihfoishgoishgioesn
    nameme = 'Pirates Hat'
    hp = 0
    dfn = 0
    atk = 0
    pihat = items(nameme, hp, dfn, atk)
    return pihat
pihat = phat()

#Shark Fin
def Sharkfin():#BJSOIUHFIHOIFDHSAOIUHFOIUSHFSIUHFIOSUHFOSIUHSOHSOFIhoiahofiaoih
    nameme = 'Sharks Fin'
    hp = 0
    dfn = 0
    atk = 0
    sharkfin = items(nameme, hp, dfn, atk)
    return sharkfin
sfin = Sharkfin()


#marsh
#Generic item from the mych randomized
def gweapon():#sehdifhcifibhsufgcsuyfsiuyfiushfoiushgoihsoiughsoihgsoihgosih
    nameme = '(Generic Weapon)'
    hp = Randomizer.ran110()
    dfn = 0
    atk = 0
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
    hp = 0
    dfn = 0
    atk = 0
    ga = items(nameme, hp, dfn, atk)
    return ga
ga = genacc()

#castle
#From cv
def food():
    nameme = 'Bread'
    hp = 0
    dfn = 0
    atk = 0
    Bread = items(nameme, hp, dfn, atk)
    return Bread
bread = food()

#hades crab lol
def hcrab():
    nameme = "Hades Crab"
    hp = 0
    dfn = 0
    atk = 0
    hc = items(nameme, hp, dfn, atk)
    return hc
hc = hcrab()

#mountains
#from pp
def persbles():#siuhfihsvfichsifhsiohfciuwhsfiuchsiufhcsiuhfsiuchsdggsdg
    nameme = "Persephone's Blessing"
    hp = 0
    dfn = 0
    atk = 0
    pb = items(nameme, hp, dfn, atk)
    return pb
pb = persbles()

#from zeus
def Lbolt():
    nameme = 'Lightning Bolt'
    hp = 0
    dfn = 0
    atk = 0
    lb = items(nameme, hp, dfn, atk)
    return lb
lb = Lbolt()

#boss
def lores():
    nameme = 'Lore'
    hp = 0
    dfn = 0
    atk = 0
    lore = items(nameme, hp, dfn, atk)
    return lore
lore = lores()

#hell
def cerb():
    nameme = 'Cerberus'
    hp = 0
    dfn = 0
    atk = 0
    dog = items(nameme, hp, dfn, atk)
    return dog
dog = cerb()

#from village
#barbarian
def club():
    nameme = 'Wooden Club'
    hp = 0
    dfn = 0
    atk = 0
    wc = items(nameme, hp, dfn, atk)
    return wc
wc = club()

#wizard
def wand():
    nameme = 'Magic Stick'
    hp = 0
    dfn = 0
    atk = 0
    stick = items(nameme, hp, dfn, atk)
    return stick
stick = wand()

#knight
def sword():
    nameme = 'Training Sword'
    hp = 0
    dfn = 0
    atk = 0
    ts = items(nameme, hp, dfn, atk)
    return ts
ts = sword()

#rogue
def dagger():
    nameme = 'Rusty Dagger'
    hp = 0
    dfn = 0
    atk = 0
    rd = items(nameme, hp, dfn, atk)
    return rd
rd = dagger()