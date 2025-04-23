# arr1 = [4,6,8]
# arr2 = [5,10,15]
arr1 = [3, 5, 7]
arr2 = [10, 15, 20]
output =[0]*len(arr1)
for i in range(len(arr1)):
    if arr1[i]%arr2[i]==0:
        output[i]=-1
    else:
        diff = arr2[i]-arr1[i]
        if diff>=arr1[i]:
            if diff==2 or diff==3 or diff==5 or diff==7 or diff%2!=0 and diff%3!=0 and diff%5!=0 and diff%7!=0:
                output[i]=diff
            else:
                output[i]=-1
        else:
            output[i]=-1

print(output)