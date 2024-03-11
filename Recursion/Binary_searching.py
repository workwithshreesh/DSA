def binary_searching(x,arr,start,end):
    if(start>end):
        return -1
    mid=(start+end)//2

    if(arr[mid]==x):
        print(mid)
    elif(arr[mid]>x):
        binary_searching(x,arr,start,mid-1)
    else:
        binary_searching(x,arr,mid+1,end)

arr=[1,2,3,4,5,6,7,8,9]
x=4
end=len(arr)-1
start=0

binary_searching(x,arr,start,end)
