# First method of number is palindrome
inpu=int(input("Enter a number:"))
temp=inpu # store input copy for checking reverse number is equal to input number or not
rev=0

while(inpu>0):
    rev=(rev*10)+inpu%10
    inpu=inpu//10

if (rev==temp):
    print("Number is palindrome")
else:
    print("Number is not palindrome")