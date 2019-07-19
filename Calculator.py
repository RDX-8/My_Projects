while True:
    N1=int(input("Enter the first no.:"))
    CAL=(input("Enter the calculation and only use +,-,=,/,÷,*,**,<,>,:"))
    N2=int(input("Enter the second no,:"))
    if CAL ==  '+':
        print(N1+N2)
    elif CAL ==  '-':
        print(N1-N2)
    elif CAL ==  '=':
        if N1 == N2:
            print("True, they are equal")
        elif N1 != N2:
            print("False, they are not equal")
    elif CAL ==  '/':
        print(N1/N2)
    elif CAL ==  '÷':
        print(N1/N2)
    elif CAL ==  '*':
        print(N1*N2)
    elif CAL ==  '**':
        print(N1**N2)
    elif CAL == '>':
        if N1>N2:
            print("True")
        else:
            print("False")
    elif CAL == '<':
        if N1<N2:
            print("True")
        else:
            print("False")
    else:
        print("?")
    q =(input("Press 1 to quit and 2 to stay"))
    if q ==  1:
        break
    if q != 1 or 2:
        print("?")
