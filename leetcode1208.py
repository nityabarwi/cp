def equalSubstring(s, t, maxCost):
    n = len(s)
    cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
    
    start = 0
    currentCost = 0
    maxLength = 0
    
    for end in range(n):
        currentCost += cost[end]
        
        while currentCost > maxCost:
            currentCost -= cost[start]
            start += 1
        
        maxLength = max(maxLength, end - start + 1)
    
    return maxLength

print(equalSubstring("abcd", "bcdf", 3))  # Output: 3
print(equalSubstring("abcd", "cdef", 3))  # Output: 1

