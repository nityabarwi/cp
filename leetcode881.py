def numRescueBoats(people, limit):
  people.sort()
  count = 0
  left, right = 0, len(people) - 1
  
  while(left <= right):
    remaining = limit - people[right]
    right -= 1
    count += 1
    if(left <= right ) and remaining >= people[left]:
      left += 1
      
  return count

people1 = [3,2,2,1]
limit1 = 3
print(numRescueBoats(people1, limit1))    #Output = 3 boats (1, 2), (2) and (3)
