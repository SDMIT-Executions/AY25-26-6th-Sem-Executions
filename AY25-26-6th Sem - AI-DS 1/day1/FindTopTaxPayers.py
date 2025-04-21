# finding the top two tax payers for auditing purpose
taxpayers = [15.6,2.7,8.9,14.5,9.2,12.7,1.9,19.7,25.9,1.2]
fTop, sTop = 0,0 

for index in range(len(taxpayers)):
    # find the fTop
    if fTop < taxpayers[index]:
        sTop = fTop
        fTop = taxpayers[index]
    elif sTop < taxpayers[index] and taxpayers[index]!=fTop:
        sTop = taxpayers[index]

print(fTop,sTop)
