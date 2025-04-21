# find distnict values

numbers = [131, 11, 48]
generated = [False,False,False,False,False,False,False,False,False,False]

# find the unique values
for each in numbers:
    while each > 0:
        digit = int(each%10)
        generated[digit]=True
        each //= 10
for index in range(len(generated)):
    if generated[index]:
        print(index,end=" ")