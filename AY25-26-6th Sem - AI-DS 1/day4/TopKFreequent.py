# find top k freequent digits in list

def findFreequent(myList,window):
    if len(myList)<2:
        print(1)
        return
    myTable = {}
    for every in myList:myTable[every] = myTable.get(every,0)+1
    myTable = sorted(myTable.items(),key=lambda each:each[1],reverse=True)
    for position in range(window):
        print(myTable[position][0], end=" ")
    print()

findFreequent([1,1,1,2,2,3],2)
findFreequent([1],1)
findFreequent([4,4,4,6,6,6,6,3,3,3,3,3],2)
findFreequent([7,7,7,8,8,9,9,9,10,10,10,10],3)
findFreequent([5,5,6,7,7,7,8,8,8,8,9],4)