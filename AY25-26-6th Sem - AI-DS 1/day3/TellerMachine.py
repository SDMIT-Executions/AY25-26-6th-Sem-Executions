# Teller machine to dispense required cash from available denomination

# def dispense(denominations,required):
#     denominations.sort(reverse=True)
#     index = 0
#     count = 0
#     while index < len(denominations):
#         if required>=denominations[index]:
#             required-=denominations[index]
#             count+=1
#         else:
#             index+=1
#     return count if required==0 else -1

def dispense(denominations,required):
    poss = [required+1]*(required+1)
    poss[0] = 0
    for currency in denominations:
        for index in range(currency,len(poss)):
            poss[index] = min(poss[index],poss[index-currency]+1)
    return poss[required] if poss[required]<required else -1

print(dispense([100,500,200],200))
# print(dispense([100,500,200],1100))
# print(dispense([100,500,200],8700))
# print(dispense([100,500,200],1950))