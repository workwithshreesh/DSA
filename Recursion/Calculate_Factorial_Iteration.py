# First method to calculate the factorial using iteration
count=1
n=int(input("Enter input: "))

for i in range(n):
    count+=count*i
    print(count)


# Second method to calculate the factorial with iteration
count=1
sum=1
n=int(input("Enter a number:"))
while(n>count):
    sum+=sum*count
    print(sum)
    count+=1


sum=0
count1=1
count2=2
n=int(input("Enter a number"))
while(n>count1):
    sum=count1*count2
    print(sum)
    count1+=1
    count2+=1

