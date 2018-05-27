# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def __init__(self):
        self.reverseList = []

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.mod_rec(str(x))
        res_str = ""
        for i in range(len(self.reverseList)):
            res_str = self.reverseList[i] + res_str
        res_int = int(res_str)
        if x < 0:
            res_int = res_int * -1
        if res_int < -2**31 or res_int > (2**31 - 1) or res_int == 0:
            return 0

        return res_int

    def mod_rec(self, target):
        if len(target) == 0 or target[-1] == "-":
            return
        else:
            self.reverseList.insert(0, (target[-1]))
            return self.mod_rec(target[:-1])
