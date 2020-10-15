class Solution:
    def isContain(self, striped_haystack: str, needle: str)->bool:
        if len(striped_haystack) < len(needle):
            return False

        for i in range(len(needle)):
            if striped_haystack[i] != needle[i]:
                return False

        return True

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if self.isContain(haystack[i:len(haystack)],needle):
                    return i

        return -1
