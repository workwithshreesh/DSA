def fibonacci(n):
    if (n<=1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))


# def fibonacci(n,a,b):
#     if n==0:
#         return 0
#     c=a+b
#     print(c)
#     fibonacci(n-1,b,c)
#
# a,b=0,1
# print(a)
# print(b)
# n=7
# fibonacci(n-2,a,b)