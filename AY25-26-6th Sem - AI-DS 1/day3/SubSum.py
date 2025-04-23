# arr = [2,-4,1,9,-6,7,-3]
arr = [2,-4,5,-2]
def SubSum(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return max(SubSum(arr[1:]),SubSum(arr[:-1]),sum(arr))
print(SubSum(arr))