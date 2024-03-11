def paranthesis(string):
    stack=[]

    for char in string:
        if char in '({[':
            stack.append(char)

        elif char is ')':
            if (not stack or stack[-1]!='('):
                return False
            stack.pop()

        elif char is ']':
            if (not stack or stack[-1]!='['):
                return False
            stack.pop()

        elif char is '}':
            if (not stack or stack[-1]!='{'):
                return False
            stack.pop()

    if (not stack):
        return True
    else:
        return False

string=input("Enter:")
ans=paranthesis(string)
print(ans)
