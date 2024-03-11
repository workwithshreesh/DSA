def stairCase(n):
    if n<0:
        return 0
    if n==0:
        return 1
    x=stairCase(n-1)
    y=stairCase(n-2)
    z=stairCase(n-3)

    return x+y+z

print(stairCase(5))