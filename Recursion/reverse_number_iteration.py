# First method of reverse number program

# Taking input by user
inpu=int(input("Enter a number:"))
rev=0  # rev is for storing the reverse value of program

# condition
while(inpu>0):
    rev=(rev*10)+inpu%10
    inpu=inpu//10

print(f"Reverse number is {rev}")