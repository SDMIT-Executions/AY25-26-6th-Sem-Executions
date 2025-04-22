A="tcs"
B="tata service"

def StringChecker(source,phrase):
    sources = iter(source)
    return all(each in sources for each in phrase)

print(1 if StringChecker(B,A) else 0)
    
# def StringChecker(A,B):
#     i=j=0
#     while i<len(A) and j<len(B):
#         if A[i]==B[j]:
#             i+=1
#             j+=1
#         else:
#             j+=1
#     if i==len(A):
#         return 1
#     else:
#         return 0
# print(StringChecker(A,B))