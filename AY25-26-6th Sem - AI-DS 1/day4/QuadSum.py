def is_quad_sum_found(arr, size, target, count, selected):
    print("current target",target,"current count",count,"selected",selected)
    if target == 0 and count == 4:
        print("found",tuple(sorted(selected)))  # Print the quadruplet
        return True
    if count > 4 or size == 0:
        return False
    # Include current element
    found_with_current = is_quad_sum_found(arr, size - 1, 
            target - arr[size - 1], count + 1, selected + [arr[size - 1]])
    # Exclude current element
    found_without_current = is_quad_sum_found(arr, size - 1, 
                                              target, count, selected)
    # return True if any pass
    return found_with_current or found_without_current

# Driver function
numbers = [2, 7, 4, 0, 9, 5, 1, 3]
print("Below are the quadruplets with sum 20:")
is_quad_sum_found(numbers, len(numbers), 20, 0, [])