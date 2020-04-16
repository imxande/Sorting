# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
   
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base case
    if len(arr) == 1:
        return arr
    # divide array in half (2 arrays)
    mid = len(arr)//2

    #slicing here to get the left and right size
    left = merge_sort(arr[:mid]) 
    right = merge_sort(arr[mid:])

    return merge(left, right)


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
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
