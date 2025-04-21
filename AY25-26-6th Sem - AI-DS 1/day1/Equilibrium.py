# find the Equilibrium index

# numbers = [-7, 1, 5, 2, -4, 3, 0]
numbers = [0,-3,5,-4,-2,3,1,0]

totalSum = sum(numbers)
partSum = 0

for index in range(len(numbers)):
    totalSum -= numbers[index]
    if totalSum == partSum:
        print(index)
        break
    else:
        partSum+=numbers[index]
