# find two sum against the target and returns their index+1

def findIndices(myList,myTarget):
    start,end = 0,len(myList)-1
    while start < end:
        sum = myList[start] + myList[end]
        if sum == myTarget: 
            print(start+1,end+1)
            return
        elif sum>myTarget: end-=1
        else: start+=1

findIndices([2,7,11,15],9)