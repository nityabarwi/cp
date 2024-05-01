def reversePrefix(word, ch):
    n = len(word)
    a = 0
    for i in range(n):
        a += 1
        if word[i] == ch:
            break
    

    strr = word[a-1::-1]
    rev = word[a:n-1:]
    return strr + rev
    
print(reversePrefix("abcd", "z"))