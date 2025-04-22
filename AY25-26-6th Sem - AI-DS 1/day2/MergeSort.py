# merge sort

def sort(source):
    if len(source) <= 1:
        return source
    # mid 
    mid = len(source)//2
    # logn
    left = sort(source[:mid])
    right = sort(source[mid:])
    # n
    return merge(left,right)

def merge(left,right):
    merged = []
    pointLeft=0
    pointRight=0
    
    while pointLeft<len(left) and pointRight<len(right):
        if left[pointLeft] <= right[pointRight]:
            merged.append(right[pointRight])
            pointRight+=1
        else:
            merged.append(left[pointLeft])
            pointLeft+=1
    
    # append remianing
    merged.extend(left[pointLeft:])
    merged.extend(right[pointRight:])
    
    return merged
    

myList = [1, 2, 3, 5, 4, 7, 12]
myList = sort(myList)
print(myList)