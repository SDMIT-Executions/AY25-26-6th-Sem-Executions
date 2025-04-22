# find moves to change X in O

def convert(source):
    move=0
    index=0
    while index < len(source):
        if source[index] == 'X' or source[index] == 'x':
            index+=3
            move+=1
        else:
            index+=1
    return move

print(convert('XXOX'))
print(convert('XXX'))
print(convert('XOXOX'))
print(convert('OOOO'))