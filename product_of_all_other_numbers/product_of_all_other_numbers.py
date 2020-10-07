'''
Input: a List of integers
Returns: a List of integers
O(n) time and O(n) space without using division

'''
import math

def product_of_all_other_numbers(arr):
    # multiply all elements except the current index
    # iterate through the array and use all elements except index
    # how to do that in O(n) time?
    # multiply numbers to the left of index by numbers to right of index

    result_list = []
    for index in range(0, len(arr)):
        if index == 0:
            result_list.append(math.prod(arr[index + 1:]))
        elif index < len(arr):
            result_list.append(math.prod(arr[:index]) * math.prod(arr[index + 1:]))
        else:
            result_list.append(math.prod(arr[:index]))
    return result_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
