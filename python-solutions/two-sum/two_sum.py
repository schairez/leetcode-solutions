#! python3

__author__ = "Sergio Chairez"
__title__ = "Two Sum"

from typing import Dict, List
"""
********************************************************************************** 
Title: Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

NOTE:  You may assume that each input would have exactly one solution, and you may not use the same element twice.

EX: Given nums = [2, 7, 11, 15], target = 9,
B/C nums[0] + nums[1] = 2 + 7 = 9; where 9 == target 
return [0, 1]
********************************************************************************** 
NOTES:
# The obvious solution is to brute-force and do 0(N^2) comparisons
# but an efficient solution would

CONCEPTS:
complement - the number to add to make the target 
EX: X + Y = target, then Y is X's complement to meet target

X = target - Y 
[2, 7, 11, 15], t =13

iter:
comp = 13 -2 = 11
store: d[comp] = idx ; d[11] = 0

comp = 13 - 7 = 6
store: d[comp] = idx; d[6] = 1 

comp = 13 - 11 = 2 
store: d[comp] = idx; d[2] = 2
********************************************************************************** 

"""
# algo explained:
# iterate through the elems in nums_array
# use the elem as the dict_key  --- `complement_key`
# use the number as the key as well as index as value


def two_sum(nums_array: List[int], target: int) -> List[int]:
    complements_d = dict()
    for idx, elem in enumerate(nums_array):
        complement_key = target - elem
        if elem in complements_d.keys():
            print(complements_d)
            return [complements_d[elem], idx]
        complements_d[complement_key] = idx


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 13
    print(two_sum(nums, target))  # [0, 2]
