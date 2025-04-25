# validating parathesis where * considered as open,close even empty

def validate(expression):
    open_count,close_count=0,0
    for each in expression:
        if each == '(': 
            open_count+=1
            close_count+=1
        elif each == ')':
            open_count = max(0,open_count-1)
            close_count -= 1
        else:
            open_count = max(0,open_count-1)
            close_count += 1
        if close_count<0: return False
    if open_count == 0: return True

print(validate("()"))
print(validate("(*))"))
print(validate("((*)"))
print(validate("(((**)"))
print(validate("(()))"))