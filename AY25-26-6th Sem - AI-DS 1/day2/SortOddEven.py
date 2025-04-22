def sortOddNEven(overall):
    # destructure overall by odd and even
    oddList = [num for num in overall if num%2!=0]
    evenList = [num for num in overall if num%2==0]
    # sort odd reverse order and even in ascending
    oddList.sort(reverse=True)
    evenList.sort()
    # replace in the overall
    overall[:len(oddList)+1] = oddList[:]
    overall[len(oddList):] = evenList[:]
    

myList = [1, 2, 3, 5, 4, 7, 10]
sortOddNEven(myList)
print(myList)
myList = [0, 4, 5, 3, 7, 2, 1]
sortOddNEven(myList)
print(myList)