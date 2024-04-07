def checkValidString(s: str) -> bool:
    # Stack to store indices of '(' and '*'
    left_stack = []
    star_stack = []
    
    for i, char in enumerate(s):
        if char == '(':
            left_stack.append(i)
        elif char == '*':
            star_stack.append(i)
        else:  # char == ')'
            if left_stack:
                left_stack.pop()  # Match '(' with ')'
            elif star_stack:
                star_stack.pop()  # Use '*' as '('
            else:
                return False
    
    # Matching remaining '(' and '*' from the stacks
    while left_stack and star_stack:
        if left_stack[-1] < star_stack[-1]:
            left_stack.pop()
            star_stack.pop()
        else:
            break
    
    # If any '(' left unmatched, the string is invalid
    return len(left_stack) == 0

s = "(*))"
print(checkValidString(s))  # Output: True
