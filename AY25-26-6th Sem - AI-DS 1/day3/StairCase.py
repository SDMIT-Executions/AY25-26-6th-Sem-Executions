# Climbing stairs possibility

def possViaDC(case):
    if case == 1: return 1
    elif case == 2: return 2
    else:
        return possViaDC(case-1)+possViaDC(case-2)

def possViaDP(case):
    if case <= 0: return 0
    elif case == 1: return 1
    elif case == 2: return 2
    else:
        possiblity=[0]*(case+1)
        possiblity[0]=0
        possiblity[1]=1
        possiblity[2]=2
        for pos in range(3,len(possiblity)):
            possiblity[pos]=possiblity[pos-1]+possiblity[pos-2]
        return possiblity[case]

print(possViaDP(5))
print(possViaDP(3))
print(possViaDP(7))

print(possViaDC(5))
print(possViaDC(3))
print(possViaDC(7))