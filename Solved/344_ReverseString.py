class Solution:
    # def reverseString(self, s: List[str]) -> None:
    def reverseString(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """

        tmp = []
        for i in range(len(s)):
            j = len(s)-i-1
            tmp.append(s[j])

        for i in range(len(s)):
            s[i] = tmp[i]
