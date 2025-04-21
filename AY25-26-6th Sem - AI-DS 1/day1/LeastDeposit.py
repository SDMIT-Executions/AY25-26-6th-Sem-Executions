# finding the least deposit of the day

deposits = [0,0,0,0,0,0,0,0,0,0,0]
minValue = 100000000000000000

# collect the deposits from 10 customers 
for position in range(1,11):
    deposits[position] = int(input("tell us the amount to deposit "))
    if minValue>deposits[position]:
        minValue=deposits[position]

print(minValue)