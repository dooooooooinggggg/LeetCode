# In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

# Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

# Example :
# Input:
# [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
# Note:

# The length of A will be in the range [1, 30].
# A[i] will be in the range of [0, 10000].


class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        target = "0" * len(A)

        while int(target, 2) <= 2**len(A):
            # print('this:%d' % int(target, 2))
            # print('end :%d' % len(A))
            B = []
            C = []
            for i in range(len(A)):
                # print('init target = %s' % (target))
                # print(target[i])
                if target[i] == "0":
                    B.append(A[i])
                else:
                    C.append(A[i])
            target = bin(int(target, 2) + 1)[2:]
            target = (len(A) - len(target)) * "0" + target
            # print('end target = %s' % (target))
            # print('B:%s, C:%s' % (B, C))

            if len(B) * len(C) != 0 and sum(B) / len(B) == sum(C) / len(C):
                print('B%s:,C:%s, avg = %f' % (B, C, sum(B) / len(B)))
                return True

        return False
