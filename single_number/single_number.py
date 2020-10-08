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

import time
import random
import operator

def first_pass(arr):

    # ------------ FIRST PASS CODE -----------------------------
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
    

    # My question with this solution, is if this is going through
    # the array only once.  The complexity is probably something like
    # O(nlogn^n) over the array, depending on Python's "not in" implementation.
    # Nothing was stated in the instructions about the time complexity.

    # --------------- REFACTORED CODE ------------------------
    # Create a dictionary and store the counts of the elements
    # Run through the array once:
        # If the key does not exist, make one and set the value to zero
        # Increment the value count by 1
    # Find the minimum of the counts in the dictionary and return its value

def single_number(arr):
    count_dict = {}

    for element in arr:
        if element not in count_dict:
            count_dict[element] = 0
        count_dict[element] += 1
    
    unique_number = min(count_dict.items(), key=operator.itemgetter(1))[0]
    return unique_number
    
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    arr2 = []
    for i in range(20, 20000):
        if i != 12345:
            arr2.insert(random.randint(0,len(arr2)), i)
            arr2.insert(random.randint(0,len(arr2)), i)
    arr2.insert(random.randint(0,len(arr2)),12345)

    # start_time = time.time()
    # result = first_pass(arr2)
    # end_time = time.time()
    # print(f"The odd-number-out is {result} with runtime of: {end_time - start_time}\n")

    start_time = time.time()
    result = single_number(arr2)
    end_time = time.time()
    print(f"The odd-number-out is {result} with runtime of: {end_time - start_time}\n")
