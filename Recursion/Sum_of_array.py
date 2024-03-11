def sumArr(arr,sum):
    lenth=len(arr)
    if (lenth==0 or lenth==1):
        sum+=arr[0]
        print(sum)
        return 0

    if arr[0]:
        sum+=arr[0]
    next=arr[1:]
    sumArr(next,sum)


arr=[1,2,3,4,5]
sumArr(arr,0)



def sumArr(n,arr,sum):
    if (n==len(arr)):
        print(sum)
        return 0
    sum+=arr[n]
    sumArr(n+1,arr,sum)

sumArr(0,arr,0)

