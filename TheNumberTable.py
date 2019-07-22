TheNum = int(input("Which numbers table do you want?"))
TheTimesNum = int(input("How many times do you want the number to mutiply"))

TheCount = 0

TheTimes = 1

while TheCount < TheTimesNum:
    A = TheNum * TheTimes
    print(A)
    TheCount += 1
    TheTimes += 1