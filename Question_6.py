#!/bin/usr/env python

""" Write a Python class to find the three elements that sum to zero from a set of n real numbers. """

# Method 1

class py_solution:
    def sum_to_zero(self, nums):
        
        nums = sorted(nums)
        result = []
        i = 0
        
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result
        
print(py_solution().sum_to_zero([-25, -10, -7, -3, 2, 4, 8, 10]))