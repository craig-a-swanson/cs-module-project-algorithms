'''
Input: a List of integers
Returns: a List of integers
'''

# -------------- FIRST PASS ------------------------------------
def first_pass(arr):
    # Iterate on the enumerated array
    # if the value is zero, remove it from the array and append it
    # check to see if all elements [index:] are zeroes, if so stop.

    # Upon testing, it was necessary to wait to pop the zeroes until the
    # end of the array was reached. To do this:
    # keep track of the indexes of the zeroes, then when the
    # end is reached, go back and pop each zero from the list.
    # The indexes change as the popping occurs -- account for that.

    # list to keep track of zero indexes in the array
    zero_indexes = []

    for index, element in enumerate(arr):
        # if the rest of the list is all zeroes, then clean up the list
        # by popping the zeroes we have come across and return the result
        if all(zero_check == 0 for zero_check in arr[index:]):
            for count, zero_index in enumerate(zero_indexes):
                arr.pop(zero_index - count)
            return arr
        # else, if the current element is zero, store its index
        # and append a zero to the current array
        elif element == 0:
            zero_indexes.append(index)
            arr.append(element)
    return arr


# ---------------- REFACTORED METHOD ------------------------------
def abolute_val(element):
    return abs(element)

def moving_zeroes(arr):
    # Complete a reversed sort on the array.
    # Need to account for negative integers in the array.
    sorted_arr = sorted(arr, key=abolute_val, reverse=True)
    return sorted_arr

# ----------------- FUTURE REFACTOR ----------------------------
# For an O(1) space complexity, we could do an in place merge sort
# Use absolute values for integers and do a reverse sort.
# Time complexity would be O(nlogn)


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    arr2 = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr2)}")