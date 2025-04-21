# finding first missing invoice

invoice = [0,1,2,4,5,6,7]

min = invoice[0]

# finding min value
for pos in range(1,len(invoice)):
    if min>invoice[pos]:
        min = invoice[pos]

# find missing
while True:
    temp = min+1
    if temp in invoice:
        min  = temp
    else:
        print(temp)
        break