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

    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        water = (j - i) * min(height[i], height[j])

        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        firstPotentialZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[firstPotentialZero], nums[i] = nums[i], nums[firstPotentialZero]
                firstPotentialZero += 1

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
        """
        return list(str(int(''.join(str(x) for x in digits)) + 1))

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
        """
        s = set(nums)
        for i, n in enumerate(nums):
            other = target - n
            if other in s:
                index = nums.index(other)
                if index != i:
                    return [i, index]


if __name__ == '__main__':
    print("Running...")
    # print(Solution().productExceptSelf([1, 2, 3, 4]))
    # print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(Solution().fourSumCount(
    #     [0, 1, -1],
    #     [-1, 1, 0],
    #     [0, 0, 1],
    #     [-1, 1, 1]
    # ))
    # print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # print(Solution().maxArea([1, 0, 0, 0, 0, 0, 0, 2, 2]))
    # assert Solution().maxArea([2, 3, 10, 5, 7, 8, 9]) == 36
    # assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    # Solution().moveZeroes([0, 1, 0, 3, 12])
    # Solution().plusOne([1, 2, 3])
    # print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([2, 7, 11, 15], 9))
