# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # TO-DO
    # Initialize pointers
    a = 0
    b = 0
    for i in range(elements):
    # Compare the first element of A and B
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base case
    if len(arr) <= 1:
        return arr
    # split array in half (2 arrays)
    mid = len(arr)//2
    # Recursion happening here
    left = merge_sort(arr[:mid]) 
    right = merge_sort(arr[mid:])

    # calling merge helper function to merge this two sorted array into one sorted array
    return merge(left, right)

# sanity check
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(arr1)
print(merge_sort(arr1))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
