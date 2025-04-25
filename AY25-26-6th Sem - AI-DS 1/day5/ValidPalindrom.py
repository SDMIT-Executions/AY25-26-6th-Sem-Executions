#check valic palindrom
from re import sub

def validateSentence(sentence):
    sentence = sub(r"[^A-Za-z0-9]","",sentence).lower()
    return True if sentence==sentence[::-1] else False

print(validateSentence("A man, a plan, a canal: Panama"))
print(validateSentence("race a car"))
print(validateSentence("A,b,ba"))

def ValidPalindrome(string):
    output =""
    for i in string:
        if i.isalpha():
            output+=i.lower()
        else:
            continue
    output2=output[::-1]
    if output==output2:
        return True
    else:
        return False
# print(ValidPalindrome("A,bba"))