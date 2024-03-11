# First method of sum of cube number
inpu=int(input("Enter your number:"))
len_inpu=len(str(inpu))
temp=inpu
sum=0
while(inpu>0):
    sum+=(inpu%10)**len_inpu
    inpu=inpu//10

if (temp==sum):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")


# Second method of sum of cube number
inpu=int(input("Enter a number:"))
len_inpu=len(str(inpu))
original_input=inpu
sum=0
while(inpu>0):
    sum+=(inpu%10)**len_inpu
    inpu//=10
print(sum)

if (original_input==sum):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")



# Third method of number is armstrong

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = 0

    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits

    return armstrong_sum == number


# Fourth method of number is armstrong

def armstrong(number):
    str_num=str(number)
    len_num=len(str_num)
    sum=0

    for digit in str_num:
        sum+=int(digit)**len_num

    if (number==sum):
        print("Number is armstrong")
    else:
        print("Number is not armstrong")

armstrong(1634)