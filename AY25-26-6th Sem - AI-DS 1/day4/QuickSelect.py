'''
len(arr) - k 
Index 0 → 7   (smallest)    >> k=5>> 5-5>> 0
Index 1 → 14
Index 2 → 15
Index 3 → 20  (2nd largest) >> k=2>> 5-2>> 3
Index 4 → 23  (largest) >> k=1>> 5-1>>4
'''
def partition(arr, start, end):
    pivot = arr[end]  # Choose last element as pivot
    left = start - 1
    for point in range(start, end):
        if arr[point] <= pivot:
            left += 1
            arr[left], arr[point] = arr[point], arr[left]  # Swap smaller element to the left
    arr[left + 1], arr[end] = arr[end], arr[left + 1]  # Move pivot to correct position
    return left + 1  # Return the pivot index

def quick_select(arr, start, end, k):
    if start == end:return arr[start]
    pivotal_point = partition(arr, start, end)
    if pivotal_point == k:return arr[pivotal_point]
    elif pivotal_point < k:return quick_select(arr, pivotal_point + 1, end, k)
    else:return quick_select(arr, start, pivotal_point - 1, k)

# Example usage
arr = [14, 23, 7, 15, 20]
k = int(input("Tell us k-th package from placement history: "))
print(quick_select(arr, 0, len(arr) - 1, len(arr)-k))
print(arr)