# validate the given strings are anagram or not

def isAnagram(word1,word2):
    if len(word1)!=len(word2):
        return False
    tableWord1 = {}
    for each in word1: tableWord1[each] = tableWord1.get(each,0)+1
    tableWord2 = {}
    for each in word2: tableWord2[each] = tableWord2.get(each,0)+1
    return True if tableWord1==tableWord2 else False

print(isAnagram("listen","silent"))
print(isAnagram("cat","rat"))
print(isAnagram("car","ark"))
print(isAnagram("ate","eat"))

# s='anagram'
# t='nagaram'
# s=sorted(s)
# t=sorted(t)
# if s==t:
#     print(True)
# else:
#     print(False)