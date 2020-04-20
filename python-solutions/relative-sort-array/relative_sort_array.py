"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Constraints:
- arr1.length, arr2.length <= 1000
- 0 <= arr1[i], arr2[i] <= 1000
- Each arr2[i] is distinct.
- Each arr2[i] is in arr1.

"""
from typing import List


def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    lookup = {v: i for i, v in enumerate(arr2)}
    print(lookup)
    return sorted(arr1, key=lambda i: lookup.get(i, len(arr2)+i))


if __name__ == "__main__":
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(relative_sort_array(arr1, arr2))
