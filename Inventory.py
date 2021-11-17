class pinv:
    def __init__(self, boat1, medhead, m_c, phat, Sharkfin, gweapon, kth, genacc, food, wcrab, persbles, clegs, lores, cerb, club, wand, sword, dagger, wcrab2):
        self.boat1 = boat1
        self.medhead = medhead
        self.m_c = m_c
        self.phat = phat
        self.Sharkfin = Sharkfin
        self.gweapon = gweapon
        self.kth = kth
        self.genacc = genacc
        self.food = food
        self.wcrab = wcrab
        self.persbles = persbles
        self.clegs = clegs
        self.lores = lores
        self.cerb = cerb
        self.club = club
        self.wand = wand
        self.sword = sword
        self.dagger = dagger
        self.wcrab2 = wcrab2

def main_inventory():
    boat1 = 'no'
    medhead = 'no'
    m_c = 'no'
    phat = 'no'
    Sharkfin = 'no'
    gweapon = 'no'
    kth = 'no'
    genacc = 'no'
    food = 'no'
    wcrab = 'no'
    persbles = 'no'
    clegs = 'no'
    lores = 'no'
    cerb = 'no'
    club = 'no'
    wand = 'no'
    sword = 'no'
    dagger = 'no'
    wcrab2 = 'no'
    minv = pinv(boat1, medhead, m_c, phat, Sharkfin, gweapon, kth, genacc, food, wcrab, persbles, clegs, lores, cerb, club, wand,sword, dagger, wcrab2)
    return minv

minv = main_inventory()









