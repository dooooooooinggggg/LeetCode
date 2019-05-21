class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(triangle)):
            res += min(triangle[i])
        return res
