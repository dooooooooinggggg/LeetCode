# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        str_0 = strs[0]
        striped_strs = strs[1:len(strs)]

        past_prefix = ""
        for i in range(1, len(str_0)+1):
            for s in striped_strs:
                if s[0:i] != str_0[0:i]:
                    return past_prefix
            past_prefix = str_0[0:i]

        return past_prefix
