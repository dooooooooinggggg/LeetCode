class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permuteRec(nums, 0, [])

    def permuteRec(self, nums, index, res):
        if (index == len(nums) - 1):
            return res
