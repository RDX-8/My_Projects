TheNumSen = int(input("How many numbers?"))
TheNum = 0
TheList = []
while TheNum <= 19:
    TheNum += 1
    TheList.append(TheNum)

TheSen = int(input("Enter a number between"))
if TheSen > TheNumSen:
    print("Invalid")

elif TheSen < 1:
    print("Invalid")

else:
    TheList.remove(TheSen)
    print(TheList)
    print("Removed the Number!")
 