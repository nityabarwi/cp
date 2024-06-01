def scoreOfString(s):
        
  score = 0
        
  for i in range(len(s) - 1):
    score += abs(ord(s[i]) - ord(s[i + 1]))

  return score

print(scoreOfString("hello"))              #output : 13

print(scoreOfString("zaz"))                #output : 50
