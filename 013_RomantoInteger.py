# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Example 1:

# Input: "III"
# Output: 3


# Example 2:

# Input: "IV"
# Output: 4


# Example 3:

# Input: "IX"
# Output: 9


# Example 4:

# Input: "LVIII"
# Output: 58
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.


# Example 5:

# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"M": 1000, "D": 500, "C": 100,
                 "L": 50, "X": 10, "V": 5, "I": 1}
        res_int = 0

        for i in range(len(s)):
            if i == len(s) - 1:
                res_int += roman[s[i]]
                break

            res_int += roman[s[i]] if roman[s[i]
                                            ] >= roman[s[i+1]] else -roman[s[i]]

        return res_int
