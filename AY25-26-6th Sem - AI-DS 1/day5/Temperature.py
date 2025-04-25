# find the number of days to wait for warmer temp than current day

def forecast(wether):
    myOutCome = [0] * len(wether)
    stack = []
    for index in range(len(wether)):
        while stack and wether[stack[-1]]<=wether[index]:
            popped = stack.pop()
            myOutCome[popped] = index - popped
        stack.append(index)
    return myOutCome

print(forecast([73,74,75,71,69,72,76,73]))
print(forecast([30,40,50,60]))
print(forecast([87,81,89,75,92]))