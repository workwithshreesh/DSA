# First method of selection sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the remaining unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index=j

        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
print(selection_sort([3,1,7,6,5,8]))
