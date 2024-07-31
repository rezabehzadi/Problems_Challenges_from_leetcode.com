"""
Description:

Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

import os

# Solution 1:
# def twoSum(nums,target):
#     for i in range(len(nums)):
#         val = target-nums[i]
#         for j in range(i+1,len(nums)):
#             if val == nums[j]:
#                 return [i, j]

# Solution 2:
# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
#     return []

# Solution 3:
def twoSum(nums, target):
    _nums = {}
    length = len(nums)
    for i in range(length):
        val = target-nums[i]
        if val in _nums:
            return [i, _nums[val]]
        _nums[nums[i]]=i


nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))