def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

    i+=1
    temp=arr[i]
    arr[i]=pivot
    arr[high]=temp
    return i

def quick_sort(arr,low,high):
    if low<high:
        pidx=partition(arr,low,high)

        quick_sort(arr,low,pidx-1)
        quick_sort(arr,pidx+1,high)

arr=[1,4,7,6,5,3,4,9,2]
high=len(arr)-1
quick_sort(arr,0,high)
print(arr)