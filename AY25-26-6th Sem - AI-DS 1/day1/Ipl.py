# moving all zero at last
stats =[20,0,4,6,0,6,0]

valid = 0
for current in range(len(stats)):
    if stats[current]!=0:
        stats[valid]=stats[current]
        valid+=1

stats[valid:] = [0] * (len(stats)-valid)

print(stats)

# out=[]
# ct=0
# for i in list:
#     if i==0:
#         ct+=1
#     else:
#         out.append(i)
# finalOuptput=out+[0]*ct
# print(finalOuptput)

