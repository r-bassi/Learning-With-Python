# Python binary search program (recursive)
# returns index of x in arr if it exists, else returns -1
def bin_search_rec(arr, first, last, x):

    # base case check
    if last >= first:

        mid = first + (last - first) // 2

        # if element is at mid, return it

        if arr[mid] == x:
            return mid

        #if element is smaller than mid, its in the left subarray

        elif arr[mid] > x:
            return bin_search_rec(arr, first, mid-1, x)


        # else the element is in the right subarray

        else:
            return bin_search_rec(arr, mid+1, last, x)

# # Example def
# arr = [1, 2, 3, 4, 5, 6, 7] 
# x = 2
  
# # Test call 
# result = bin_search_rec(arr, 0, len(arr)-1, x) 
  
# if result != -1: 
#     print ("Element exists at index % d" % result) 

# else: 
#     print ("Element does not exist in the array") 