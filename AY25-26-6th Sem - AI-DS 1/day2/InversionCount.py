# find the inversion count for e-commerce inefficiency

def mergeCount(orders):
    if len(orders) <= 1:
        return orders,0
    mid = len(orders)//2
    left,leftCount = mergeCount(orders[:mid])
    right,rightCount = mergeCount(orders[mid:])
    merged, mergedCount = mergeInversion(left,right)
    return merged,leftCount+mergedCount+rightCount

def mergeInversion(left,right):
    merged = []
    pointerLeft=0
    pointerRight=0
    currentInversion = 0
    while pointerLeft<len(left) and pointerRight<len(right):
        if left[pointerLeft]<=right[pointerRight]:
            merged.append(left[pointerLeft])
            pointerLeft+=1
        else:
            merged.append(right[pointerRight])
            pointerRight+=1
            currentInversion += (len(left)-pointerLeft)
    merged.extend(left[pointerLeft:])
    merged.extend(right[pointerRight:])
    
    return merged, currentInversion
    
def brute_force(orders):
    inversions = 0
    for selected in range(len(orders)):
        for compare in range(selected,len(orders)):
            if orders[selected]>orders[compare]:
                inversions += 1
    return inversions

myOrders = [30, 45, 25, 60, 20]
print(mergeCount(myOrders))
print(brute_force(myOrders))