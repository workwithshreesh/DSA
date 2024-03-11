def printnum_nto1(n):
    if (n==0):
        return 0
    print(n)
    printnum_nto1(n-1)

printnum_nto1(5)

