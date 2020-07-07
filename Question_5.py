#!/bin/usr/env python

""" Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. """

# Method 1

class my_solution:
    def find_pair(self, pair_list, tar):
        for i in pair_list:
            temp = i
            for t in pair_list:
                if t + temp == tar:
                    index1 = pair_list.index(t)
                    index2 = pair_list.index(temp)
                    print(index1, index2)
                    break
                break
            
my_solution().find_pair([10,20,10,40,59,60,70], 20)

# Method 2

class py_solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
            
print("index1 = %d, index2 = %d" % py_solution().twoSum((10,20,10,40,50,60,70),20))