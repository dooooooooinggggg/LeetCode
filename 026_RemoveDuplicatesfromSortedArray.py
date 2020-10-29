class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        now = nums[0]
        for i in range(1, len(nums)):
            print(nums)
            if now != nums[i]:
                now = nums[i]
            else:
                nums.pop(i)
        return
