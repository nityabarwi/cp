def beautifulSubsets(nums, k):
    def backtrack(start, current_list):
        nonlocal count
        if current_list:
            count += 1
        for i in range(start, len(nums)):
            if all(abs(nums[i] - x) != k for x in current_list):
                current_list.append(nums[i])
                backtrack(i + 1, current_list)
                current_list.pop()  # Remove the last element to backtrack

    count = 0
    nums.sort()
    backtrack(0, [])
    return count

nums1 = [2, 4, 6]
k1 = 2
print(beautifulSubsets(nums1, k1))  # Output: 4
