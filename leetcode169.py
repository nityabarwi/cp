def majorityElement(nums: list[int]) -> int:
    nums.sort()
    mid = len(nums)
    a = nums[mid//2]
    return a

print(majorityElement([2,2,1,1,1,2,2]))