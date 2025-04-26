def insert_interval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    # Add all intervals before `newInterval` (non-overlapping & sorted)
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    # Add remaining non-overlapping intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    return result

# Test cases
print(insert_interval([[1,3],[6,9]], [2,5]))  # Output: [[1,5],[6,9]]
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # Output: [[1,2],[3,10],[12,16]]
