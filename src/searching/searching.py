def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] != target:
            i+= 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (right + left) // 2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
           right =  middle - 1
        else:
            left = middle + 1


    return -1  # not found
