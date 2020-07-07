#!/usr/bin/env python

import itertools

""" Write a Python class to get all possible unique subsets from a set of distinct integers. """

# Method 1

class my_solution:
    # Define function to acquire list of values (num).
    def unique_subsets(self, num):
        # Loop through list of values (num).
        for i in range(0, len(num) + 1):
            # Loop through combination of iterations generated from initial values (num).
            for subset in itertools.combinations(num, i):
                print(subset)
        
        
my_solution().unique_subsets([4,5,6])

# Method 2

class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
    
print(py_solution().sub_sets([4,5,6]))