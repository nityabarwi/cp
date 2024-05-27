def specialArray(nums):
    nums.sort()
    n = len(nums)
    
    for x in range(n + 1):
        # Find how many numbers are >= x
        count = sum(num >= x for num in nums)
        if count == x:
            return x
            
    return -1
