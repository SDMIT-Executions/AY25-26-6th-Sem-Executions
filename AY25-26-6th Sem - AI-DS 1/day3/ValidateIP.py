# validating IPV4

def isValidIP(ip):
    segments = ip.split(".")
    if len(segments)<4:
        return False
    for each in segments:
        if str.isdigit(each):   
            temp = int(each)
            if temp<0 and temp>255 or str(temp)!=each:
                return False
        else: return False
    return True

print(isValidIP("222.111.111.111"))
print(isValidIP("5555..555"))
print(isValidIP("0.0.0.0255"))
print(isValidIP("0.0.0.0"))