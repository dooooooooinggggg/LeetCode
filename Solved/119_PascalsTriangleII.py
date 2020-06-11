class Solution:
    # def getRow(self, rowIndex: int) -> List[int]:
    def getRow(self, rowIndex: int):
        i = 0
        p = []
        p.append([1])
        for i in range(1, rowIndex+1):
            ikkoue = p[i-1]
            tmp_l = []
            for j in range(i+1):
                if j == 0:
                    tmp_l.append(ikkoue[0])
                elif j == len(ikkoue):
                    tmp_l.append(ikkoue[-1])
                else:
                    tmp_l.append(ikkoue[j-1]+ikkoue[j])
            p.append(tmp_l)
        return p[-1]
