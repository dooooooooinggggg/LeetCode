# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        all_list = []
        all_list.extend(nums1)
        all_list.extend(nums2)
        all_list.sort()

        len_all = len(all_list)
        if len_all % 2 != 0:
            i = int((len_all - 1) / 2)
            res = all_list[i]
        else:
            i1 = int(len_all / 2) - 1
            i2 = int(len_all / 2)
            res = (all_list[i1] + all_list[i2]) / 2

        return float(res)
