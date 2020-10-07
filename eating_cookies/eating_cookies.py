'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = {}):
    # Your code here
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n not in cache:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
