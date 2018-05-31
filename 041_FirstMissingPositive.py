# Given an unsorted integer array, find the smallest missing positive integer.
# Note:
# Your algorithm should run in O(n) time and uses constant extra space.


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == []:
            return 1

        nums.sort()
        for i in range(max(nums)+1):
            if i+1 not in nums:
                return i+1
