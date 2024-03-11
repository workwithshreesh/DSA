def binary_search(x,arr,start,end):
    if (start>end):
        return -1

    mid=(start+end)//2

    if arr[mid]==x:
        print(mid)

    elif arr[mid]>x:
        binary_search(x,arr,start,mid-1)
    else:
        binary_search(x,arr,mid+1,end)


x=4
arr=[1,2,3,4,5,6,7]
start=0
end=len(arr)-1

binary_search(x,arr,start,end)



def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)


print(fact(5))

inpu=5
rev=1
for i in range(1,inpu):
    rev+=rev*i

print(rev)


inpu=5
rev=1
while(inpu>0):
    inpu -= 1
    rev+=rev*inpu

print(rev)


def fibonacci(n):
    if n<=1:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(4))

def fibonacci(a,b,n):
    if n==0:
        return 0

    c=a+b
    print(c)
    fibonacci(b,c,n-1)

a,b=0,1
print(a)
print(b)
n=7
fibonacci(a,b,n-2)



def SumNatural(n,sum):
    if (n==0):
        print(sum)
        return 0

    sum+=n
    SumNatural(n-1,sum)

SumNatural(5,0)


def SumNatural(n,base,sum):
    if n==base:
        sum+=n
        print(sum)
        return 0

    SumNatural(n+1,base,sum+n)

SumNatural(1,5,0)



n=123
rev=0
while (n>0):
    rev=rev*10+(n%10)
    n=n//10

print(rev)


def numrev(n,rev):
    if n==0:
        print(rev)
        return 0

    rev=rev*10+(n%10)
    numrev(n//10,rev)

numrev(123,0)



def NumRev(n): #wrong
    if (n<10):
        return n
    else:
        last_digit=n//10
        remaining_digit=NumRev(n%10)
        return str(remaining_digit)+str(last_digit)

print(NumRev(123))


# num is palindrome
def numpalin(n,rev,temp):
    if temp is None:
        temp=n
    if n==0:
        if temp==rev:
            print(f"Number is Palindrome {rev}")
        else:
            print(f"Number is not Palindrome {rev}")
        return

    rev=rev*10+(n%10)
    numpalin(n//10,rev,temp)


n=212
rev=0
temp=None
numpalin(n,rev,temp)


def NumArm(n,sum,temp):
    temp_len=len(str(temp))
    if n==0:
        if temp==sum:
            print("Number is armstrong")
        else:
            print("Number is not armstrong")
        return 0
    sum+=(n%10)**temp_len
    NumArm(n//10,sum,temp)

sum,n=0,155
temp=n
NumArm(n,sum,temp)


def countZero(n,x):
    if n==0:
        print(x)
        return 0
    if (n%10)==0:
        x+=1
    countZero(n//10,x)

countZero(60007650,0)


def first_index(n,x,arr):
    if n==len(arr)-1:
        return 0

    if arr[n]==x:
        print(n)
    else:
        first_index(n+1,x,arr)

arr=[1,2,3,4,5,2,6,7]
x=4
n=0
first_index(n,x,arr)



def last_index(arr,x):
    if len(arr)==0:
        return -1

    smalloutput=arr[1:]
    smallist=last_index(smalloutput,x)
    if smallist!=-1:
        return smallist+1
    else:
        if arr[0]==x:
            return 0
        else:
            return -1

arr=[1,2,3,4,5,4,7]
x=4
print(last_index(arr,x))



keypad=['.','abc','def','ghi','jkl','mno','pqr','stu','wx','yz']
def keypad_combination(mystr,index,combination):
    global keypad
    if index==len(mystr):
        print(combination)
        return 0

    currChar=mystr[index]
    mapping=keypad[ord(currChar)-ord('0')]

    for i in range(len(mapping)):
        keypad_combination(mystr,index+1,combination+mapping[i])

mystr='3'
index=0
keypad_combination(mystr,index,'')



def tower_hanoi(n,src,helper,dest):
    if n==1:
        print(f"disk {n} moved from {src} to {dest}")
        return 0

    tower_hanoi(n-1,src,dest,helper)
    print(f"disk {n} moved from {src} to {dest}")
    tower_hanoi(n-1,helper,src,dest)

tower_hanoi(3,'s','h','d')


def replaceChar(strings,char,x):
    if len(strings)==0:
        return strings

    smallOutput=replaceChar(strings[1:],char,x)

    if strings[0]==char:
        return x+smallOutput
    else:
        return strings[0]+smallOutput

print(replaceChar('sshhrrsshh','r','p'))


def replaceChar(strings,char,char1,xn):
    if len(strings)==0 or len(strings)==1:
        return strings

    smalloutput=replaceChar(strings[1:],char,char1,xn)

    if strings[0]==char or strings[0]==char1:
        return xn+smalloutput
    else:
        return strings[0]+smalloutput


print(replaceChar('ssbbhhrreess','h','e','p'))


def replaceChar(strings,char1,char2,x):
    if len(strings)==0 or len(strings)==1:
        return strings

    smalloutput=replaceChar(strings[1:],char1,char2,x)

    if strings[0]==char1 and strings[1]==char2:
        return x+smalloutput
    else:
        return strings[0]+smalloutput

strings='shssjfhjpihsjdjpip'
char1='p'
char2='i'
x='xd'
print(replaceChar(strings,char1,char2,x))


#Liked list


