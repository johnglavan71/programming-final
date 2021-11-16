from time import sleep
print("'Hello there young man, I have heard of your travels and it seems to me you're looking for something.\n"
      "I am Charon, you can think of me as a ferryman. I can give souls a ride straight to Hades.' ")
sleep(2.5)
cha = input("I have here a key, a key that can bring you to a special place. Would you like me to take you?\n"
            "yes or no? : ")
if cha == "yes" or cha == "Yes" or cha == "YES":
    print("'Very well then, follow me.......\n")
    sleep(2)
    print(      "\n"
          "\n"
          " to the last place you will ever see'")
    sleep(4)
    # underworld
elif cha == "no" or cha == "No" or cha == "NO":
    sleep(1)
    print("'Very well, I am sure I'll be watching, I mean see you later..'")
else:
    print("'BOY, DID YOU NOT HEAR ME!!!!!!'")
