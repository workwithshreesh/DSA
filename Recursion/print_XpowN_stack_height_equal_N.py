def printpower(x,n):
    if (n==0):
        return 1
    if (x==0):
        return 0
    call_func=printpower(x,n-1)
    execute=x*call_func
    return execute

x,n=2,5

first_call=printpower(x,n)
print(first_call)