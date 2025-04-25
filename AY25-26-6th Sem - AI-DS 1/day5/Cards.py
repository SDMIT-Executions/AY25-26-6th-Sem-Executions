# grouping the cards with given window size

def grouping(myList,myWindow):
    if not len(myList)%myWindow==0: return False
    myTable = {}
    for each in myList: myTable[each] = myTable.get(each,0)+1
    sorted_items = sorted(myTable.keys())
    for num in sorted_items:
        while myTable[num] > 0:
            for index in range(num,num+myWindow):
                if myTable.get(index,0) == 0:
                    return False
                myTable[index]-=1
    return True

print(grouping([1,2,3,6,2,3,4,7,8],3))
print(grouping([1,2,3,4,5],4))
