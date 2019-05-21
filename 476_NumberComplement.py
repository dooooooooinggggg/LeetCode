# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res_str = ""
        for i in range(2, len(bin(num))):
            res_str += "0" if bin(num)[i] == "1" else "1"

        return int(res_str, 2)
