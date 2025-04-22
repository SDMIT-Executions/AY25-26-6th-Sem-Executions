# sorting via recursion

def findSum(origin):
    if not origin:
        return 0
    return origin[0]+findSum(origin[1:])

total = findSum([900,20,450,210,60])
print(total)