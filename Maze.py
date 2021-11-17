from Fights import mazef
from time import sleep


def mazepath():
    print("You see what looks like an entrance into a hallway of overgrown threes.")
    sleep(2)
    m = input("Do you enter? Yes or No? : ")
    if m == "yes" or m == "Yes":
        m = input("Do you want to go straight, left, or back? S or L or B : ")
        if m == "L" or m == "l":#1
            m = input("Do you want to go left, straight, right, or back? L or S or R or B : ")
            if m == "R" or m == "r":#2
                m = input("Do you want to go left, straight, right, or back? L or S or R or B : ")
                if m == "L" or m == "l":#3
                    m = input("Do you want to go straight, right, or back? S or R or B : ")
                    if m == "R" or m == "r":#4
                        m = input("Do you want to go straight, right, or back? S or R or B : ")
                        if m == "R" or m == "r":#5
                            m = input("Do you want to go left, straight, or back? L or S or B : ")
                            if m == "L" or m == "l":#6
                                m = input("Do you want to go left, right, or back? L or R or B : ")
                                if m == "L" or m == "l":#7
                                    m = input("Do you want to go left, straight, right, or back? L or S or R or B : ")
                                    if m == "R" or m == "r":#8
                                        m = input("Do you want to go left, straight, right, or back? L or S or R or B : ")
                                        if m == "S" or m == "s":#9
                                            m = input("Do you want to go straight, right, or back? S or R or B : ")
                                            if m == "R" or m == "r":#10
                                                m = input("Do you want to go left, straight, or back? L or S or B : ")
                                                if m == "L" or m == "l":#11
                                                    print("You've reached the end of the maze and see a woman with snakes for hair.... you approach.")
                                                    q = 1
                                                    return q
                                                else:
                                                    print('You Pass out in the maze and wake up at the entrance.')
                                                    mazepath()
                                            else:
                                                print('You Pass out in the maze and wake up at the entrance.')
                                                mazepath()
                                        else:
                                            print('You Pass out in the maze and wake up at the entrance.')
                                            mazepath()
                                    else:
                                        print('You Pass out in the maze and wake up at the entrance.')
                                        mazepath()
                                else:
                                    print('You Pass out in the maze and wake up at the entrance.')
                                    mazepath()
                            else:
                                print('You Pass out in the maze and wake up at the entrance.')
                                mazepath()
                        else:
                            print('You Pass out in the maze and wake up at the entrance.')
                            mazepath()
                    elif m == "S" or m == "s":
                        m = input("Do you want to go left, straight, right, or back? L or S or R or B : ")
                        if m == "l" or m == "L":
                            m = input("Do you want to go left, straight, right, or back? L or S or R or B : ")
                            if m == "R" or m == "r":
                                m = input("Do you want to go left, straight, right, or back? L or S or R or B : ")
                                if m == "L" or m == "l":
                                    m = input("Do you want to go left, straight, right, or back? L or S or R or B : ")
                                    if m == "R" or m == "r":
                                        print("You have found a secret area within the maze. You see a scroll... it reads\n"
                                              "'If player types (admin) when picking class, it makes player unbeatable.\n"
                                              "To try restart game.'")
                                        mazepath()
                    else:
                        print('You Pass out in the maze and wake up at the entrance.')
                        mazepath()
                else:
                    print('You Pass out in the maze and wake up at the entrance.')
                    mazepath()
            else:
                print('You Pass out in the maze and wake up at the entrance.')
                mazepath()
        else:
            print('You Pass out in the maze and wake up at the entrance.')
            mazepath()
    elif m == "No" or m == "no":
        print("You turn back and continue your journey.")
        p = 2
        return p
    else:
        print("You turn back and continue your journey.")
        p = 2
        return p

