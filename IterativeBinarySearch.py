# Python binary search function (iterative)
# returns index of x in arr if it exists, else returns -1
# works for arrays that are already sorted

def bin_search_iter(arr, x):
    first = 0
    last = len(arr)-1
    mid = 0

    while first <= last:

        mid = (first + last) // 2

        # Check if x exists at mid
        if arr[mid] < x:
            first = mid + 1

        # If x is larger, ignore left subarray
        elif arr[mid] > x:
            last = mid -1

        # If x is smaller, ignore right subarray
        else:
            return mid

    # The element was not present in the array
    return -1


    # Example def
arr = [1, 2, 3, 4, 5, 6, 7] 
x = 2
  
# Test call 
result = bin_search_iter(arr, x) 
  
if result != -1: 
    print ("Element exists at index % d" % result) 

else: 
    print ("Element does not exist in the array") 