# First Method one to print a 1 to n number by using recursion.
def one_to_n(n,a):
    if (n<=a):
        print(n)
    if (n==a):
        return 0
    one_to_n(n+1,a)

one_to_n(1,6)

print()

# Second Method one to print a 1 to n number by using recursion.
def one_to_n(n):
    if (n==0):
        return 0
    one_to_n(n-1)
    print(n)

one_to_n(5)


print()

# Third Method one to print a 1 to n number by using recursion.
def one_to_n(n):
    if (n>6):
        return 0
    print(n)
    one_to_n(n+1)

one_to_n(1)