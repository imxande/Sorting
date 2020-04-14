# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        temp = arr[i]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] <  arr[smallest_index]:
                smallest_index = j
          
        # TO-DO: swap
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # need a temporary variable to swap
        temp = arr[i]
        # in order to compare I need to loop again
        for j in range(0, len(arr) - 1):
            # checking if right hand side is less the left hand side
            if arr[j] > arr[j + 1]:
                # stored the right hand side value into variable so I can use that spot
                temp = arr[j + 1]
                # copy the left hand side value into the right hand side one
                arr[j + 1] = arr[j]
                # the left hand side value now gets the value stored in the temporary variable to complete the swap
                arr[j] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# sanity check
myArray = [3, 4, 2, 5, 6, 10, 8, 7, 9, 1]
# print(selection_sort(myArray))
print(bubble_sort(myArray))