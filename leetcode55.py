def jump(nums):
  n = len(nums)
  reachable = 0
  for i in range(n):
    if reachable < i:
      return False
    reachable = max(reachable, i + nums[i])
  return True

nums1 = [2,3,1,1,4]
print(jump(nums1))       #True

nums2 = [3,2,1,0,4]
print(jump(nums2))       #False
