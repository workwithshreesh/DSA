def strickly_increasing_array(array,indx):
    if indx==len(array)-1:
        return True

    if(array[indx]<array[indx+1]):
        return strickly_increasing_array(array,indx+1)
    else:
        print(False)

arr=[1,2,3]
print(strickly_increasing_array(arr,0))




def isSorted(arr,indx):
    # Base case
    if(indx==len(arr)-1):
        return True

    if(arr[indx]>=arr[indx+1]):
        return False

    return isSorted(arr, indx + 1)

arr=[1,2,3,4]
print(isSorted(arr,0))






def isSorted(a):
    l=len(a)
    if l==0 or l==1:
        return True

    if a[0]>a[1]:
        return False

    smallerList=a[1:]
    isSmallerList=isSorted(smallerList)
    if isSmallerList:
        return True
    else:
        return False

print(isSorted([1,2,3,4,5,6,7,8]))