
"""
two-positive integers r and c representing the row and col respectively

using the 'reshape' operation w/ given params is 


product has to stay the same; else default to original matrix

r, c range [1,100];
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]

* Use matrix[index / width][index % width] for both matrices

"""
from typing import List

# (matrix: List[List[int]], r: int, c: int) -> List[List[int]]:


def matrix_reshape(orig_matrix: List[List[int]], r: int, c: int) -> List[List[int]]:
    origR = len(orig_matrix)
    origC = len(orig_matrix[0])
    if origR * origC != r * c:
        return orig_matrix
    count = 0
    result_arr = [[0 for _ in range(c)] for _ in range(r)]
    for row in range(len(orig_matrix)):
        for col in range(len(orig_matrix[0])):
            print(orig_matrix[row][col])
            result_arr[count // c][count % c] = orig_matrix[row][col]
    return result_arr


if __name__ == "__main__":
    nums = [[1, 2],
            [3, 4]]
    print(len(nums))
    print(nums[0])
    print(matrix_reshape(nums, 1, 4))
