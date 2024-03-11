# First method of number is armstrong

def num_armstrong(n,sum,temp):
    tem_len=len(str(temp))
    if (n==0):
        if (temp==sum):
            print("Number is armstrong")
        else:
            print("Number is not armstrong")
        return 0
    sum+=(n%10)**tem_len
    num_armstrong(n//10,sum,temp)

n=155
temp=n
sum=0
num_armstrong(n,sum,temp)


# Second method of number is armstrong

def is_armstrong_number_recursive(number, power=None,temp=None,sum=0):
    if power is None:
        power = len(str(number))

    if temp is None:
         temp=number

    last_digit = number % 10
    remaining_number = number // 10
    sum+=last_digit ** power

    if number==0:
        if (temp == sum):
            print("Number is armstrong")
        else:
            print("Number is not armstrong")
        return 0

    is_armstrong_number_recursive(remaining_number, power,temp,sum)

is_armstrong_number_recursive(1634)