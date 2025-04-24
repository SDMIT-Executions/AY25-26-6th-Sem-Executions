from collections import deque

def max_result(nums, k):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_deque = deque([0])
    for i in range(1, n):
        while max_deque and max_deque[0] < i - k:
            max_deque.popleft()
        dp[i] = dp[max_deque[0]] + nums[i]
        while max_deque and dp[i] >= dp[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(i)
    return dp[-1]

# Test cases
nums1 = [1, -1, -2, 4, -7, 3]
k1 = 2
print(max_result(nums1, k1))  # Output: 7

nums2 = [10, -5, -2, 4, 0, 3]
k2 = 3
print(max_result(nums2, k2))  # Output: 17

nums3 = [1, -5, -20, 4, -1, 3, -6, -3]
k3 = 2
print(max_result(nums3, k3))  # Output: 0
