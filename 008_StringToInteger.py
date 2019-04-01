class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        s = str.replace(" ", "")
        if len(s) == 0 or s == "+":
            return 0

        # minus check
        isNotMinus = 1
        if s[0] == "-":
            isNotMinus = -1
        s = s.replace("-", "")

        if (len(s) == 0) or (isNotMinus == -1 and s[0] == "+"):
            return 0

        tmp = ""
        for i in range(len(s)):
            if s[i] in numbers:
                tmp += s[i]
            elif s[i] == "+":
                continue
            else:
                if tmp == "":
                    return 0
                break

        res = int(tmp) * isNotMinus

        if (res < -2147483648):
            res = -2147483648
        if (res > 2147483648):
            res = 2147483648

        return res
