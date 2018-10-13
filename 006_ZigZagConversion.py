class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        numRows = 5
        a = []
        for i in range(numRows-1):
            if(i == 0):
                a += [True]*numRows
            else:
                tmp = []
                tmp += [False]*numRows
                tmp[numRows - (i+1)] = True
                a.extend(tmp)
        a = self.rec_len_a_fix(a, s)

        index = 0
        for i in range(len(a)):
            if(a[i]):
                a[i] = s[index]
                index += 1
                if index >= len(s):
                    break
        res = ""
        for i in range(numRows):
            i2 = 0
            while(True):
                this_index = i*i2
                if (this_index > len(a)):
                    break
                if(a[this_index]):
                    res += a[this_index]
                i2 += 1

        print(res)

    def rec_len_a_fix(self, a, s):
        tmp = [i for i in a if i]
        if (len(tmp) > len(s)):
            return a
        else:
            a.extend(a)
            return self.rec_len_a_fix(a, s)
