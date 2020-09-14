# takes a sorted array as input and a target to search for 
# and returns the index of the target in the array if it 
# exists, or -1 if the element is not in the array
def binary_search(arr, target):
    # find the midpoint element 
    # length // 2
    left = 0
    right = len(arr) - 1

    # keep iterating so long as left <= right
    while left <= right:
        midpoint = (right + left) // 2

        if arr[midpoint] == target:
            return midpoint

        elif arr[midpoint] > target:
            # toss out the left side of the array 
            # toss out the midpoint element itself as well 
            right = midpoint - 1

        else:
            left = midpoint + 1

    # we didn't find what we're looking for 
    return -1


arr = [3,4,6,16,26,28,52,55]
print(binary_search(arr, 100))
