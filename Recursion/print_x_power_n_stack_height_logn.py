def lognpower(x,n):
    if (n==0):
        return 1
    if (x==0):
        return 0

    if (n%2==0):
        return lognpower(x,n//2)*lognpower(x,n//2)
    else:
        return lognpower(x,n//2)*lognpower(x,n//2)*x


x=2
n=5
calcpower=lognpower(x,n)
print(calcpower)