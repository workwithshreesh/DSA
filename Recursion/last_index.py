def lastIndex(arr,x):
    if(len(arr)==0):
        return -1

    smallerList=arr[1:]
    smallerOutput=lastIndex(smallerList,x)
    if(smallerOutput!=-1):
        return smallerOutput+1
    else:
        if(arr[0]==x):
            return 0
        else:
            return -1

arr=[1,2,3,4,5,6,7,5]
x=6
print(lastIndex(arr,x))


def lastIndex(n,arr,x):
    if(n==len(arr)):
        return -1

    smallerOutput=lastIndex(n+1,arr,x)
    if(smallerOutput!=-1):
        return smallerOutput
    else:
        if(arr[n]==x):
            return n
        else:
            return -1

arr=[1,4,3,4,5]
x=4
print(lastIndex(0,arr,x))