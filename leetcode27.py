def removeElement(nums, val):
    k = 0  # Pointer indicating the position where next non-val element should be placed
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# Test cases
nums1 = [3,2,2,3]
val1 = 3
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2

print(removeElement(nums1, val1))  # Output: 2, nums1 = [2, 2, _, _]
print(nums1)
print(removeElement(nums2, val2))  # Output: 5, nums2 = [0, 1, 4, 0, 3, _, _, _]
print(nums2)
