# Find factorial of given number using dynamic programming

def factorial(given):
    if given<=0: return 1
    else:
        possibility = [1]*(given+1)
        possibility[0] = 1
        for index in range(1,len(possibility)):
            possibility[index]=index*possibility[index-1]
        return possibility[given]

print(factorial(5))
print(factorial(7))
print(factorial(3))