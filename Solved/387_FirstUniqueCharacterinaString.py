class Solution:
    def isUnique(self, finder: str, findee: str) -> bool:
        for f in findee:
            if f == finder:
                return False
        return True

    def firstUniqChar(self, s: str) -> int:

        if len(s) == 1:
            return 0

        for c_index in range(len(s)):
            compared_s_before = s[0:c_index]
            compared_s_after = s[c_index+1:len(s)]
            if self.isUnique(s[c_index], compared_s_before+compared_s_after):
                return c_index
        return -1
