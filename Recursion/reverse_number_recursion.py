# First method of reverse number using recursion
def reverse_num(n,rev):
    if (n==0):
        print(rev)
        return 0
    rev=(rev*10)+n%10
    reverse_num(n//10,rev)

reverse_num(28,0)


# Second method of reverse number using recursion
def reverse_num(n):
    if (n<10):
        return n
    else:
        last_digit=n//10
        remaining_num=reverse_num(n%10)
        return str(remaining_num) + str(last_digit)

print(reverse_num(123))


