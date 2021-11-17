class pinv:
    def __init__(self, boat1, medhead, m_c, phat, Sharkfin, gweapon, kth, genacc, food, hcrab, persbles, Lbolt, lores, cerb, club, wand, sword, dagger):
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
        self.Lbolt = Lbolt
        self.lores = lores
        self.cerb = cerb
        self.club = club
        self.wand = wand
        self.sword = sword
        self.dagger = dagger

def main_inventory():
    r = "no"
    q = "no"
    p = "no"
    o = "no"
    n = "no"
    m = "no"
    l = "no"
    k = "no"
    j = "no"
    i = "no"
    h = "no"
    g = "no"
    f = "no"
    e = "no"
    d = "no"
    c = "no"
    b = "no"
    a = "no"
    minv = pinv(r, q, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a)

    print(minv.sword)
main_inventory()









