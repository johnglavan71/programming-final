class pinv:
    def __init__(self, boat1, medhead, m_c, phat, Sharkfin, gweapon, kth, genacc, food, hcrab, persbles, clegs, lores, cerb, club, wand, sword, dagger):
        self.boat1 = boat1
        self.medhead = medhead
        self.m_c = m_c
        self.phat = phat
        self.Sharkfin = Sharkfin
        self.gweapon = gweapon
        self.kth = kth
        self.genacc = genacc
        self.food = food
        self.hcrab = hcrab
        self.persbles = persbles
        self.clegs = clegs
        self.lores = lores
        self.cerb = cerb
        self.club = club
        self.wand = wand
        self.sword = sword
        self.dagger = dagger

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
    hcrab = 'no'
    persbles = 'no'
    clegs = 'no'
    lores = 'no'
    cerb = 'no'
    club = 'no'
    wand = 'no'
    sword = 'no'
    dagger = 'no'
    minv = pinv(boat1, medhead, m_c, phat, Sharkfin, gweapon, kth, genacc, food, hcrab, persbles, clegs, lores, cerb, club, wand,sword, dagger)
    return minv

minv = main_inventory()









