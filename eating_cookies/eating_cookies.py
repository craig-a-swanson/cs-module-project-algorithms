'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache_array = []):
    # Your code here
    if cache_array == []:
        cache_array = [0 for i in range(n+1)]
    if n < 0:
        return 0
    if n == 0:
        return 1
    if cache_array[n-1] == 0:
        cache_array[n-1] = eating_cookies(n - 1, cache_array) + eating_cookies(n - 2, cache_array) + eating_cookies(n - 3, cache_array)
    return cache_array[n-1]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
