"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target):
    # Your code here
    # compare idx + (idx + 1) to target
    # if not equal, idx + 2
    idx = 1
    for num in nums:
        for num in nums:
            print (num,nums[idx])
            if num + nums[idx] == target:
                return('found:', nums.index(num), nums.index(nums[idx]))
        if idx < len(nums)-2:
            idx +=1

two_sum([4,3,5], 8)