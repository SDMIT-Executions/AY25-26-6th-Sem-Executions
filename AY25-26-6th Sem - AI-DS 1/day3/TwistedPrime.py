# find given is twisted prime

def isTwistedPrime(given):
    if given <= 1: return False
    if given==2 or given==3 or given==5 or given==7 or given%2!=0 and given%3!=0 and given%5!=0 and given%7!=0:
        # perform reverse
        temp_str = str(given)[::-1]
        mirror = int(temp_str)
        if mirror==2 or mirror==3 or mirror==5 or mirror==7 or mirror%2!=0 and mirror%3!=0 and mirror%5!=0 and mirror%7!=0:
            return True
        else:
            return False
    else: return False

print(1 if isTwistedPrime(1) else 0)