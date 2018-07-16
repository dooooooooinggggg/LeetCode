# [-1, 0, 1, 2, -1, -4]


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i+1 <= len(nums):
                for j in range(i+1, len(nums)):
                    if i+1 <= len(nums):
                        for k in range(j+1, len(nums)):
                            if nums[i]+nums[j] + nums[k] == 0:
                                tmp = [nums[i], nums[j], nums[k]]
                                tmp.sort()
                                if tmp not in res:
                                    res.append(tmp)
                                # print(res)
        return res
