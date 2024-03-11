def multiplication(m,n,a=0):
    if n==1:
        a+=m
        print(a)
        return 0
    a+=m
    multiplication(m,n-1,a)

multiplication(3,5)