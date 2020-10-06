'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

Non-empty array
Each number appears twice except one, which appears once
Return the number that appears once
Based on examples, array is not sorted
Algorithm should do a single pass through the array
Space complexity O(1)

'''
def single_number(arr):
    # Itereate through and call the "not in" method for each element
    # enumerate the list and call "not in" on the list before that element
    # and after that element. If both are true, that's the number we return

    for index, element in enumerate(arr):
        # special case for first element
            # don't look backward, just forward
        if index == 0:
            if element not in arr[index + 1:]:
                return element
        # otherwise, check the first part of the list, then the second part
        elif element not in arr[:index]:
            if element not in arr[index + 1:]:
                return element
    

    '''
    My question with this solution, is if this is going through
    the array only once.  The complexity is probably something like
    O(nlogn) over the array, depending on Python's "not in" implementation.
    Nothing was stated in the instructions about the time complexity.
    '''

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")