# irctc ticket priority : 0,1,2

tickets = [2,0,0,1,0,2,0,1]

start,mid,end=0,0,len(tickets)-1

while mid<=end:
    # check for 0 swap b/w s and m
    if tickets[mid]==0:
        tickets[start],tickets[mid]=tickets[mid],tickets[start]
        # tickets[start] += tickets[mid]
        # tickets[mid] = tickets[start] - tickets[mid];
        # tickets[start] -= tickets[mid];
        start+=1
        mid+=1
    # check for 1 
    elif tickets[mid]==1:
        mid+=1
    else:
        tickets[mid],tickets[end]=tickets[end],tickets[mid]
        end-=1

print(tickets)    