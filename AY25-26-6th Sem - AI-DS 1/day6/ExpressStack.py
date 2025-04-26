# using RPN evaluate expression
def process(expression):
    stack = []
    for token in expression:
        if token in ['+','-','*','/']:
            right = stack.pop()
            left = stack.pop()
            if token == '+': stack.append(left+right)
            elif token == '-': stack.append(left-right)
            elif token == '*': stack.append(left*right)
            elif token == '/': stack.append(int(left/right))
        else:stack.append(int(token))
    return stack[-1]   
# Test cases
print(process(["2","1","+","3","*"]))  # Output: 9
print(process(["4","13","5","/","+"]))  # Output: 6
print(process(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Output: 22
