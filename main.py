from typing import List


# disabling these so that solutions can be copied into leetcode without needing to change method name etc.
# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution(object):

    def productExceptSelf(self, nums):
        """
        Multiply left product by right product
        """
        length = len(nums)
        sol = [1] * length

        left = 1
        for i in range(1, length):
            left *= nums[i - 1]
            sol[i] = left

        right = 1
        for j in range(length - 2, -1, -1):
            right *= nums[j + 1]
            sol[j] *= right

        return sol

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Pop around the outside, rotating the matrix as we go"""
        spiral = []

        while matrix:
            spiral += matrix.pop(0)
            [row.reverse() for row in matrix]
            matrix = [list(x) for x in list(zip(*matrix))]

        return spiral

    def fourSumCount(self, A, B, C, D):
        import collections
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)


if __name__ == '__main__':
    print("Running...")
    print(Solution().productExceptSelf([1, 2, 3, 4]))
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(Solution().fourSumCount(
        [0, 1, -1],
        [-1, 1, 0],
        [0, 0, 1],
        [-1, 1, 1]
    ))
