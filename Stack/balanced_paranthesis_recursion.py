def isBalanced(string,stack):
    if not stack:
        return

    if string in '({[':
        stack.append(string)
