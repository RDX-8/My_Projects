import random
ThePointCom = 0
ThePointPlayer = 0
ThePoint = int(input("How many point game?(Press 0 to quit)"))
if ThePoint == 0:
    print("Bye!")
elif ThePoint > 0:
    while True:
        if ThePointCom == ThePoint:
            print("I WON!!!:) :O")
            break
        elif ThePointPlayer == ThePoint:
            print("You win:(")
            break
        
        TheSen = input("R,rock,   P,paper,     S,scissors 0 for quit")#Input is a function like print execpt the user can input anything
        TheRandomNum = random.randint(1, 3)#R 1, P 2, S 3

        if TheSen =="R":
            if TheRandomNum == 1:
              print("Nothing :/")
              continue
            elif TheRandomNum == 2:
                print ("I get a point :)")
                ThePointCom += 1
                continue
            elif TheRandomNum == 3:
                print ("You get a point :(")
                ThePointPlayer += 1
                continue

        elif TheSen == "P":
            if TheRandomNum == 2:
                print("Nothing :/")
                continue
            elif TheRandomNum == 3:
                print ("I get a point :)")
                ThePointCom += 1
                continue
            elif TheRandomNum == 1:
                print ("You get a point :(")
                ThePointPlayer += 1
                continue

        elif TheSen == "S":
            if TheRandomNum == 3:
                print("Nothing :/")
                continue
            elif TheRandomNum == 1:
                print ("I get a point :)")
                ThePointCom += 1
                continue
            elif TheRandomNum == 2:
                print ("You get a point :(")
                ThePointPlayer += 1
                continue
        
        elif TheSen == "0":
            print("Bye")
            break
        
        else:
            print("Enter Something Valid")
            continue