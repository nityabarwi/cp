def minRemoveToMakeValid(s: str) -> str:
    stack = []
    remove_indices = set()
    
    # First pass: identify indices of unmatched parentheses
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                remove_indices.add(i)
    
    # Second pass: add remaining unmatched opening parentheses indices
    remove_indices.update(stack)
    
    # Construct valid string
    result = ''
    for i, char in enumerate(s):
        if i not in remove_indices:
            result += char
    
    return result

# Example usage
s = "lee(t(c)o)de)"
print(minRemoveToMakeValid(s))  # Output: "lee(t(c)ode)"
