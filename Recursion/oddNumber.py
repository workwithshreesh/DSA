def oddNumber(n):
    if(n==1):
        return n
    oddNumber(n-1)
    smalloutput=(n-1)+(n-2)
    print(smalloutput)

oddNumber(5)