class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ""
        k = 0
        unsorted = T
        for i in range(len(S)):
            for j in range(len(T)):
                # print("S:"+S[i])
                # print("T:"+T[j])
                if S[i] == T[j]:
                    print(T[j] + "でmatch")
                    res += unsorted[j-k]
                    tmp1 = unsorted[0:j-k]
                    tmp2 = unsorted[j-k+1:]
                    unsorted = tmp1 + tmp2
                    print("T:"+T)
                    print("u:"+unsorted)

                    k += 1

        res += unsorted
        return res
