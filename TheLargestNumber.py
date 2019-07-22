#Write a Python program to get the largest number from a list.

TheSen1 = int(input("Enter The How many numbers"))

TheCount = 0

L1 = []

while TheCount < TheSen1:
    TheSen2 = int(input("Enter the Num"))
    L1.append(TheSen2)
    TheCount += 1


L1 = (sorted(L1, reverse = True))
print("The largest number is:", L1[0])