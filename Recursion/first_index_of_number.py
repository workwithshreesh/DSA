def firstIndex(arr,x):
    if(len(arr)==0):
        return -1
    if(arr[0]==x):
        return 0

    smallerArr=arr[1:]
    smallerOutput=firstIndex(smallerArr,x)
    if(smallerOutput==-1):
        return -1
    else:
        return smallerOutput+1

arr=[1,9,3,4,5,6,7]
x=9
print(firstIndex(arr,x))




def firstIndex(n,arr,x):
    if(n==len(arr)):
        return -1

    if(arr[n]==x):
        return 0
    increasing=n+1
    smallerOutput=firstIndex(increasing,arr,x)
    if(smallerOutput==-1):
        return -1
    else:
        return increasing+1

print(firstIndex(0,arr,x))





def firstIndex(n,arr,x):
    if(n==len(arr)):
        return -1

    if(arr[n]==x):
        return n

    output=firstIndex(n+1,arr,x)
    if(output==-1):
        return -1
    else:
        return output
arr=[1,2,3,4,5,6]
x=4
print(firstIndex(0,arr,x))



def firstIndex(n,arr,x):
    if(x not in arr):
        print(-1)
        return 0

    if(arr[n]==x):
        print(n)
        return 0

    firstIndex(n+1,arr,x)

arr=[1,2,3,4]
firstIndex(0,arr,5)




def firstIndex(n,arr,x):
    if(n==len(arr)):
        return -1
    if(arr[n]==x):
        return n

    return firstIndex(n+1,arr,x)
arr=[1,2,3,4,5,6]
print(firstIndex(0,arr,5))