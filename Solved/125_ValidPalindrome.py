class Solution:
    def isPalindrome(self, s: str) -> bool:
        filterd_s = []
        for c in s:
            # 48 <= c <= 57
            if ord(c) >= 48 and ord(c) <= 57:
                filterd_s.append(c)
                continue

            # 65 <= c <= 90
            # 97 <= c <= 122
            if ord(c) >= 65 and ord(c) <= 90:
                filterd_s.append(c.lower())
                continue
            if ord(c) >= 97 and ord(c) <= 122:
                filterd_s.append(c)

        return "".join(filterd_s) == "".join(reversed(filterd_s))
