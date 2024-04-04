def max_depth(s):
    max_depth = 0
    current_depth = 0

    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1

    return max_depth

# Test cases
s1 = "(1+(2*3)+((8)/4))+1"
s2 = "(1)+((2))+(((3)))"

print(max_depth(s1))  # Output: 3
print(max_depth(s2))  # Output: 3
