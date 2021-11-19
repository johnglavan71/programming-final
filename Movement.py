from time import sleep
import Dialogue
import Fights
from Inventory import minv
from Items import *
from Player import p
import Maze


#village    John


def village():
    print('Welcome to the the quaint little village of (Insert generic village name here). We hope you enjoy your stay!\n')
    sleep(2)
    wtd = input('What would you like to do? Talk to trader? (T) Talk to Blacksmith? (B) Go somewhere? (GO) First quest. (FQ)\n: ')
    if wtd == 'T':
        Dialogue.trader()
        village()
    elif wtd == 'B':
        Dialogue.blacksmith()
        village()
    elif wtd == 'FQ':
        Fights.fight1()
        village()
    elif wtd == 'GO':
        wtg = input("Where would you like to go? Dark Root Garden (drg) : ")
        if wtg == "drg":
            forest()
            drg()
        else:
            print('One of the villagers doesnt want you to leave yet.')
            sleep(4)
            village()
    else:
        village()

#forest     John


def forest():
    print('Warning dangerous monsters!! Stay on path the forest is dark, and you may get lost.')
    sleep(4)


def drg():
    print('You wandered into a grove of trees. The canopies are blocking the light. Keep your eyes on the ground the roots might be hard to see.\n')
    sleep(2)
    print('There doesnt seem to be anything of interest here.\n')
    sleep(2)
    wtg = input("Where would you like to go? Village, Maze, Yggdrasil (y) : ")
    if wtg == "Village":
        village()
    elif wtg == 'Maze':
        maze()
    elif wtg == 'y':
        y()
    else:
        print('You walked off the path follow the moss back to the path!!')
        sleep(2)
        drg()


def maze():
    print('You find tall trees that are grown so unnaturally close to one another. Maybe theres something under that arch over there?')
    sleep(2)
    q = Maze.mazepath()
    if q == 1:
        win = Fights.mazef()
        if win == "f":
            village()
        else:
            wtg = input("Where would you like to go? Mysterious Chasm (mc), Dense Thicket (dt), Dark Root Garden (drg) : ")
            if wtg == "mc":
                marsh()
                mc()
            elif wtg == 'dt':
                dt()
            elif wtg == 'drg':
                drg()
            else:
                print('You walked off the path follow the moss back to the path!!')
                sleep(2)
                maze()
    else:
        wtg = input("Where would you like to go? Dense Thicket (dt), Dark Root Garden (drg) : ")
        if wtg == 'dt':
            dt()
        elif wtg == 'drg':
            drg()
        else:
            print('You walked off the path follow the moss back to the path!!')
            sleep(2)
            maze()



def dt():
    print('The trees are tightly packed but you can still move through them with relative ease.')
    sleep(2)
    win = Fights.fight2()
    if win == 'f':
        village()
    else:
        wtg = input("where would you like to go? sandy shore (ss), misty marsh (mm), maze, yggdrasil (y) : ")
        if wtg == "ss":
            if minv.boat1 == 'no':
                print('you should go get a boat!')
                dt()
            else:
                ocean()
                ss()
        elif wtg == 'mm':
            marsh()
            mm()
        elif wtg == 'maze':
            maze()
        elif wtg == 'y':
            y()
        else:
            print('you walked off the path follow the moss back to the path!!')
            sleep(2)
            dt()


def y():
    print('The tree feels like its trying to talk to you. Maybe you should touch it.')
    sleep(2)
    Dialogue.yggdrasil()
    wtg = input("Where would you like to go? Cetus's Domain (cd), Dense Thicket (dt), Dark Root Garden (drg) : ")
    if wtg == "cd":
        if minv.boat1 == 'no':
            print('You dont have a boat.')
            y()
        else:
            ocean()
            cd()
    elif wtg == 'dt':
        dt()
    elif wtg == 'drg':
        drg()
    else:
        print('You walked off the path follow the moss back to the path!!')
        sleep(2)
        y()


#Ocean  Chris
def ocean():
    print("Treterous waters ahead! Beware of creatures eyeing your every move The Oceans are a dangerous place.")
    sleep(4)


def cd():
    print("You have entered Cetus's Domain. He glares at you with intent to kill.")
    sleep(2)
    win = Fights.cetusf()
    if win == "f":
        ss()
    else:
        wtg = input('Where would you like to go? Yggdrasil, Coral Reef (cr), Sandy Shore (ss) : ')
        if wtg == 'Yggdrasil':
            forest()
            y()
        elif wtg == 'cr':
            cr()
        elif wtg == 'ss':
            ss()
        else:
            print("You fell off the boat get back on quick!!!")
            sleep(2)
            cd()


def cr():
    print("You look into the ocean and see beautiful colors and lots of fish. Maybe you should go take a swim!")
    sleep(2)
    wtg = input("Where would you like to go? Deep Dark (dd), Cetus's Domain (cd), Go for a swim (Swim) : ")
    if wtg == 'dd':
        dd()
    elif wtg == "cd":
        cd()
    elif wtg =="swim":
        print('The reef has so many colorful fish and coral.')
        sleep(1)
        if minv.m_c == "yes":
            print('You already collected the best shell')
        elif minv.m_c == 'no':
            print('You pickup the best looking shell and take it with you.')
            minv.m_c = 'yes'
            print('You received', {fu.name})
            p.hp += fu.hp
            p.atk += fu.atk
            p.dfn += fu.dfn
            sleep(1)
            cr()
    else:
        print("You fell off the boat get back on quick!!!")
        sleep(2)
        cr()


def dd():
    print('The water is so deep that the water turned black. Maybe we should stay away.')
    sleep(2)
    win = Fights.sharkf()
    if win == "f":
        ss()
    else:
        wtg = input("Where would you like to go? Coral Reef (cr), Sandy Shore (ss), Port : ")
        if wtg == 'cr':
            cr()
        elif wtg == "ss":
            ss()
        elif wtg == "Port":
            port()
        else:
            print("You fell off the boat get back on quick!!!")
            sleep(2)
            dd()


def ss():
    print("You find a relaxing beach that had many shells lined on the sandy shore.")
    sleep(2)
    wtd = input("You find a happy crab roaming the beach. What do you do? Smite or Walk Away (wa) : ")
    if wtd == "smite" or wtd == "Smite":
        Fights.crabf()
    elif wtd == "wa" or wtd == "WA":
        wtg = input("Where would you like to go? Deep Dark (dd), Dense Thicket (dt), Cetus's Domain (cd) : ")
        if wtg == 'dd':
            dd()
        elif wtg == 'dt':
            forest()
            dt()
        elif wtg == 'cd':
            cd()
        else:
            print("You fell off the boat get back on quick!!!")
            sleep(2)
            ss()


def port():
    print('The port doesnt look like its ment for your type of boat. However you hear loud noises coming from the town behind it.')
    sleep(2)
    wtg = input("Where would you like to go? Deep Dark (dd), Castle Slums (cs), Forbidden Seas (fs) : ")
    if wtg == 'dd':
        dd()
    elif wtg == 'fs':
        fs()
    elif wtg == "cs":
        slums()
    else:
        print("You fell off the boat get back on quick!!!")
        sleep(2)
        port()


def fs():
    print('You start to wonder why its called the Forbidden sea. Its so calm and peaceful.')
    sleep(2)
    win = Fights.genvilf()
    if win == "f":
        ss()
    else:
        wtg = input("Where would you like to go? Port, Iron mines (im) : ")
        if wtg == 'Port':
            port()
        elif wtg == "im":
            im()
        else:
            print("You fell off the boat get back on quick!!!")
            sleep(2)
            fs()


#Marsh  John
def marsh():
    print('You slowly walk into the marsh. It feels like its sucking you in. Maybe someone knows why.')
    sleep(4)


def mm():
    print('You can barley see through the fog. Why does it feel like its going to rain?')
    sleep(2)
    win = Fights.hydraf()
    if win == "f":
        cg()
    else:
        wtg = input("Where would you like to go? Dense Thicket (dt), Mysterious Chasm (mc), Small Forest (sf) : ")
        if wtg == "dt":
            forest()
            dt()
        elif wtg == 'mc':
            mc()
        elif wtg == 'sf':
            sf()
        else:
            print('You got turned around in the cattails and found yourself right where you began.')
            sleep(2)
            mm()

        #look at other comment below    i like it feels like the best way to describe whos done what    
        #narrator laughing at charater for getting scared and looking down   


def mc():
    print('Dont look down... DONT look down... DONT LOOK down... DONT LOOK DOWN!!')
    sleep(2)
    win = Fights.darknessf()
    if win == "f":
        cg()
    else:
        #if player looks down theres nothing there and say i told you not to.
        wtg = input("Where would you like to go? Maze, Misty Marsh (mm), Small Forest(sf) : ")
        if wtg == "Maze":
            forest()
            maze()
        elif wtg == 'mm':
            mm()
        elif wtg == 'sf':
            sf()
        else:
            print('You got turned around in the cattails and found yourself right where you began.')
            sleep(2)
            mc()


def sf():
    print('You find youself in a small forest. It feels kind of odd...')
    sleep(2)
    wtg = input("Where would you like to go? Misty Marsh (mm), Mysterious Chasm (mc),\n"
                " Gloomy Bog (gb), Cypress Graveyard (cg) : ")
    if wtg == "mm":
        mm()
    elif wtg == 'mc':
        mc()
    elif wtg == 'gb':
        gb()
    elif wtg == 'cg':
        cg()
    else:
        print('You got turned around in the cattails and found yourself right where you began.')
        sleep(2)
        sf()


def gb():
    print('The ground feel almost like a sponge. Even without many trees this place still gets little sunlight.')
    sleep(2)
    win = Fights.lizardf()
    if win == "f":
        cg()
    else:
        wtg = input("Where would you like to go? Whatch Tower (wt), Cypress Graveyard (cg), Small Forest (sf) : ")
        if wtg == "wt":
            mountains()
            wt()
        elif wtg == 'cg':
            cg()
        elif wtg == 'sf':
            sf()
        else:
            print('You got turned around in the cattails and found yourself right where you began.')
            sleep(2)
            gb()


def cg():
    print('The stench is almost unbearable yet it looks like someone is standing overthere, staring?')
    sleep(2)
    if minv.wcrab == 'yes' or minv.wcrab2 == 'yes':
        talk = input('Do you wish to talk to Charon? Y/N : ')
        if talk == 'y' or talk == 'Y':
            print('I can grant you the key to hell for a price.\n The cost is 1000 gold pieces!')
            buy = ('Do you wish to buy the key? Y/N')
            if buy == 'y' or buy == 'Y':
                if p.cur < 1000:
                    print('You do not have enough money to satify me.')
                elif p.cur >= 1000:
                    p.cur -= 1000
                    minv.kth = "yes"
                    print('When in the Cypress Graveyard type in hell to go to the underworld.')
            elif buy == 'N' or buy == 'n':
                print('Very well then continue your adventures traveler.')
            else:
                print('Lets start this conversation over.')
                cg()
        elif talk == 'n' or talk == 'N':
            print('You decide to keep on walking.')
        else:
            print('Try typing correctly this is a text based game you should be used to it buy now.')
            cg()
    else:
        wtg = input("Where would you like to go? Small Forest (sf), Gloomy Bog (gb) : ")
        if wtg == "sf":
            sf()
        elif wtg == 'gb':
            gb()
        elif wtg == 'hell' or wtg == 'Hell':
            if minv.cerb == 'yes':
                print('You have no reason to go back.')
                cg()
            else:
                print('You hop in a boat and are ferried across the river styx.\n'
                      'After reaching the otherside you find a dog with 3 heads.\n'
                      'It says its looking for its owner. You decide why not it cant hurt.\n'
                      'You ferry it back across the river and is says it can smell its owner.\n'
                      'It stares intently at the castle. Maybe you should go there.')
                minv.cerb = 'yes'
                p.hp += dog.hp
                p.dfn += dog.dfn
                p.atk += dog.atk
                print('The dog says its name is Cerberus and will help you travel to the castle.')
                print(f'You now have {p.hp} health.')
                print(f'You now have {p.dfn} defence.')
                print(f'You now do {p.atk} damage.')
                cg()
        else:
            print('You got turned around in the cattails and found yourself right where you began.')
            sleep(2)
            cg()


#Mountains  Chris
def mountains():
    print("Take your time traversing the landscape The Mountains can both be beautiful and dangerous.")
    sleep(4)


def wt():
    print("There are a few guards here. I wonder how long theve been stuck at their post. Maybe they are hungry?")
    sleep(2)
    wtg = input("Where would you like to go? Gloomy Bog (gb), Zeus Peak (zp) : ")
    if wtg == 'gb':
        marsh()
        gb()
    elif wtg == 'zp':
        zp()
    else:
        print("Watch your step, Hades lurks below...")
        sleep(2)
        wt()


def zp():
    print("There is a storm at the top of the mountain and lightning keeps striking the same spot. I guess thats why its called Zues' peak.")
    sleep(2)
    if minv.Sharkfin == "yes" and minv.phat == "yes" and minv.medhead == "yes" and minv.gweapon == "yes" and minv.persbles == "yes":
        print("You have defeated the most powerful creatures in the land, it is time for your next battle.")
    else:
        wtg = input("Where would you like to go? Watch Tower (wt), Persephone's Pass (pp) : ")
        if wtg == 'wt':
            wt()
        elif wtg == "pp":
            pp()
        else:
            print("Watch your step, Hades lurks below...")
            sleep(2)
            zp()


def pp():
    print("Persephone's Pass, huh, better watch your back, it will always feel like someones watching you.")
    sleep(2)
    win = Fights.persephonef()
    if win == "f":
        wt()
    else:
        print("Watch your step, Hades lurks below...")
        sleep(2)
        pp()
        wtg = input("Where would you like to go? Zeus' Peak (zp), Iron Mines (im) : ")
        if wtg == 'zp':
            zp()
        elif wtg == "im":
            im()
        else:
            print("Watch your step, Hades lurks below...")
            sleep(2)
            pp()


def im():
    print("The Iron Mines can be a rough place, but the castle needs its iron.")
    sleep(2)
    win = Fights.kobaldf()
    if win == "f":
        wt()
    else:
        print("Watch your step, Hades lurks below...")
        sleep(2)
        im()
        wtg = input("Where would you like to go? Persephone's Pass (pp), Forbidden Seas (fs) : ")
        if wtg == 'pp':
            pp()
        elif wtg == 'fs':
            ocean()
            fs()
        else:
            print("Watch your step, Hades lurks below...")
            sleep(2)
            im()


#Castle Town    Chris and John
def ct():
    print("The looks of this part of town looks like a hellscape, but in the distance gleems a beautiful castle.")
    sleep(4)


def slums():
    print("Watch your back, The Slums have eyes everywhere.")
    sleep(2)
    wtg = input("Where would you like to go? Castle Village (cv), Port : ")
    if wtg == 'cv':
        cv()
    elif wtg == "port":
        ocean()
        port()
    else:
        print("You feel like your being watched... but nobodys there.")
        sleep(2)
        slums()


def cv():
    print("Welcome to the chaotic Castle Village, there is alot of shady looking people so keep your eyes peeled!")
    sleep(2)
    wtg = input("Where would you like to go? Slums, Castle (c) : ")
    if wtg == 'Slums':
        slums()
    elif wtg == "c":
        c()
    else:
        print("The market is big and confusing, don't get turned around")
        sleep(2)
        cv()


def c():
    print("As The Castle doors open, the lights seem to dissapear as the candle lit hallways invte you in.")
    sleep(2)
    if minv.cerb == 'yes':
        Fights.cerbf()
        c()
    else:
        wtg = input("Where would you like to go? Castle Village (cv), Nobles : ")
        if wtg == 'cv':
            cv()
        elif wtg == "Nobles":
            nobles()
        else:
            print("The castle hallway seems to loop in on itself.")
            sleep(2)
            c()


def nobles():
    print("The land of riches is a far reach from the slums, this is where the pretentious Nobles reside.")
    sleep(2)
    wtg = input("Where would you like to go? Castle, Watch Tower (wt) : ")
    if wtg == 'Castle':
        pp()
    elif wtg == 'wt':
        wt()
    else:
        print("You get lost in the mass of riches.")
        sleep(2)
        nobles()


def weasel():
    win = Fights.weaself()
    if win == 'f':
        minv.boat1 = 'no'
        minv.medhead = 'no'
        minv.m_c = 'no'
        minv.phat = 'no'
        minv.Sharkfin = 'no'
        minv.gweapon = 'no'
        minv.kth = 'no'
        minv.genacc = 'no'
        minv.food = 'no'
        minv.hcrab = 'no'
        minv.persbles = 'no'
        minv.lores = 'no'
        minv.cerb = 'no'
        minv.club = 'no'
        minv.wand = 'no'
        minv.sword = 'no'
        minv.dagger = 'no'
        p.hp = 10
        p.dfn = 0
        p.atk = 1
        p.cur = 5
        p.bsmith = 1
        print('You got royally fucked and lost everything including your stats.')
        village()
    else:
        wt()

village()
