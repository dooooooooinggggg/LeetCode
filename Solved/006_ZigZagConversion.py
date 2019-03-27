class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ""
        for i in range(numRows):
            if (i == 0 or i == numRows-1):
                while(True):
                    j = i
                    intervel = numRows+(numRows-2)
                    while(True):
                        if j > len(s)-1:
                            break
                        res += s[j]
                        j += intervel
                    break
            else:
                while(True):
                    j = i
                    intervelCounter = 0
                    intervel = self.considerIntervel(numRows, i)
                    while(True):
                        if j > len(s)-1:
                            break
                        res += s[j]
                        j += intervel[intervelCounter % 2]
                        intervelCounter += 1
                    break
        return res

    def considerIntervel(self, numRows, thisRow):
        allInterval = numRows+(numRows-2)
        second = thisRow*2
        first = allInterval - second
        return [first, second]
