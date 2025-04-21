transaction_seq=[900,1200,5600,120,450,270,100,10000,400,120]
DebitCount=0
for position in range(1,len(transaction_seq)):
    if transaction_seq[position-1]>transaction_seq[position]:
        DebitCount+=1
        
if DebitCount>3:
    DebitCount-=3
    transaction_seq[len(transaction_seq)-1]-=DebitCount*20
print(transaction_seq)
