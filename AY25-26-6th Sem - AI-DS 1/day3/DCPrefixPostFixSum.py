# # find prefix and post fix sum using dc

# O(n)
arr = [23,12,98,45,18]
n=len(arr)
preSum = [0]*n
postSum = [0]*n

for pos in range(len(arr)):
    if pos ==0:
        preSum[0]=arr[0]
        postSum[0]=arr[n-1]
    else:
        preSum[pos]=preSum[pos-1]+arr[pos]
        postSum[pos]=postSum[pos-1]+arr[n-pos-1]
        
print(preSum,postSum)




def divide_and_conquer_prefix_sum(array, start, end):
    if start == end:
        return [array[start]]  # Base case for prefix sum
    
    mid = (start + end) // 2
    left_prefix = divide_and_conquer_prefix_sum(array, start, mid)
    right_prefix = divide_and_conquer_prefix_sum(array, mid + 1, end)

    total_left_sum = left_prefix[-1]
    combined_prefix = left_prefix + [total_left_sum + x for x in right_prefix]

    return combined_prefix

def divide_and_conquer_postfix_sum(array, start, end):
    if start == end:
        return [array[start]]  # Base case for postfix sum
    
    mid = (start + end) // 2
    left_postfix = divide_and_conquer_postfix_sum(array, start, mid)
    right_postfix = divide_and_conquer_postfix_sum(array, mid + 1, end)

    total_right_sum = right_postfix[0]
    combined_postfix = [x + total_right_sum for x in left_postfix] + right_postfix

    return combined_postfix

# Example usage
balance = [23, 12, 98, 45, 18, 45, 12, 98]
prefix = divide_and_conquer_prefix_sum(balance, 0, len(balance) - 1)
postfix = divide_and_conquer_postfix_sum(balance, 0, len(balance) - 1)

print("Prefix Sum:", prefix)
print("Postfix Sum:", postfix)
