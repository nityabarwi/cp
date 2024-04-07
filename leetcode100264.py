def longestMonotonicSubarray(nums):
    ans = inc = de = 1
        
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            inc += 1
            de = 1
            ans = max(ans, inc)
        elif nums[i] < nums[i - 1]:
            inc = 1
            de += 1
            ans = max(ans, de)
        else:
            inc = 1
            de = 1
                
    return ans