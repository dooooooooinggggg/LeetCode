# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def __init__(self):
        self.now_longest_string = ""

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        arg_string = s

        while(len(arg_string) > 0):
            arg_string = self.stringAllCheck(arg_string)

        print(self.now_longest_string)
        return len(self.now_longest_string)

    def stringAllCheck(self, this_string):
        if len(this_string) == 0:
            return
        this_max = ""
        for i in range(len(this_string)):
            if this_max.count(this_string[i]) == 0:
                this_max = this_max + this_string[i]
            else:
                break

        if len(this_max) > len(self.now_longest_string):
            self.now_longest_string = this_max

        return this_string[1:]
