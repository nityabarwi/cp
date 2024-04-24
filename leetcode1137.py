def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    # Initialize memoization array with initial Tribonacci values
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    
    # Calculate Tribonacci numbers using memoization
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    
    return memo[n]

# Test cases
print(tribonacci(4))  # Output: 4
print(tribonacci(25)) # Output: 1389537
