def appendCharacters(s, t):
  ans = len(t)
  j = 0

  for i in range(len(s)):
    if j >= len(t):
      break
    if s[i] == t[j]:
      ans -= 1
      j += 1
  return ans

s1 = "coaching", t1 = "coding"
print(appendCharacters(s1, t1))        #Output: 4
            
