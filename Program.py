def binary_search(arr, x):
    l = 0
    h = len(arr) - 1
    middle = 0

    while l <= h:

        middle = (h + l) // 2


        if arr[middle] < x:
            l = middle + 1


        elif arr[middle] > x:
            h = middle - 1


        else:
            return middle


    return -1


# Test
arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = 15


result = binary_search(arr, x)


if result != -1:
    print("Element found at index", str(result))
else:
    print("Element not found in array")