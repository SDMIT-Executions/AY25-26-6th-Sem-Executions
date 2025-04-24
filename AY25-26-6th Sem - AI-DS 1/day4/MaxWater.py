heights=[1,8,6,2,5,4,8,3,7]
def AreaFinder():
    left=0
    right=(len(heights)-1)
    temp=0
    while left<right:
        if (min(heights[left],heights[right])*(right-left))>temp:
            temp=min(heights[left],heights[right])*(right-left)
        else:
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
    return temp
print(AreaFinder())











# def max_area(height):
#     left, right = 0, len(height) - 1
#     max_water = 0
#     while left < right:
#         # Calculate current container's area
#         water = (right - left) * min(height[left], height[right])
#         max_water = max(max_water, water)
#         # Move the pointer at the smaller height to maximize area
#         if height[left] < height[right]:left += 1
#         else:right -= 1
#     return max_water

# # Test cases
# print(max_area([1,8,6,2,5,4,8,3,7]))  # Output: 49
# print(max_area([1,1]))  # Output: 1