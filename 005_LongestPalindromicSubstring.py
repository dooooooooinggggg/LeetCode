class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            this_len = len(s) - i
            for j in range(len(s)):
                if j+this_len > len(s):
                    break
                this_string = s[j:j+this_len]
                if this_string[0] != this_string[-1:]:
                    continue
                if self.isKaibun(this_string):
                    return this_string
        return ""

    def isKaibun(self, s):
        lens = len(s)
        if lens % 2 == 0:
            first = s[0:lens//2]
            second = s[lens//2:]
            second_reverse = second[::-1]
        elif lens % 2 == 1:
            first = s[0:(int)(lens-1)//2]
            second = s[(lens+1)//2:]
            second_reverse = second[::-1]
        return (first == second_reverse)
