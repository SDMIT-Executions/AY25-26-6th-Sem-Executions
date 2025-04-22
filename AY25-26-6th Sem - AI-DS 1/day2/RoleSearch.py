# find rank of your role in trends using binary search

# def browse(trends,find):
#     left=0
#     right=len(trends)-1
#     while left<=right:
#         mid=(left+right)//2
#         if trends[mid]==find:
#             return mid+1
#         elif find in trends[:mid]:
#             right=mid-1
#         else:
#             left=mid+1

def browse(trends,find,start,end):
    if start<=end:
        mid = start+(end-start)//2
        if trends[mid]==find:return mid+1
        elif find in trends[:mid]:return browse(trends,find,start,mid-1)
        else: return browse(trends,find,mid+1,end)
    

google_trends = ["Java developer", "cloud architect", "data analyst", "devops engineer" ,"full stack developer", "network associate"]
search = input("enter the role to find the ranking ")
# print(browse(google_trends,search))
print(browse(google_trends,search,0,len(google_trends)-1))
