# First method of fibonacci series
x=0
y=1
z=0
count=1
n=int(input("Enter Input:"))
while(n>=count):
    x=y
    y=z
    z=x+y
    print(z,end=" ")
    count+=1

print()




# Second method of fibonacci series

n=int(input("Enter Input"))
a,b=0,1

for fibonacci in range(n):
    print(a,end=" ")

    a,b=b,a+b


print()



# Third method of fibonacci series

n=int(input('Enter Input'))
fibonacci=[0,1]

while len(fibonacci)<n:
    next_term=fibonacci[-1]+fibonacci[-2]
    fibonacci.append(next_term)

for i in fibonacci:
    print(i,end=" ")


print()

# Fourth method of fibonacci series

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b

n=int(input("Enter Input"))

for term in fibonacci(n):
    print(term,end=" ")