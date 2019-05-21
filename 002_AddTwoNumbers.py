# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res = ListNode(0)

        self.kuriage(l1, l2, res, 0)
        return res

    def kuriage(self, l1, l2, res, n):
        sum_tmp = l1.val + l2.val + n

        if sum_tmp >= 10:
            sum_this = sum_tmp - 10
            n = 1
        else:
            n = 0
            sum_this = sum_tmp

        res.val = sum_this

        if (not isinstance(l1.next, type(None))) and (not isinstance(l2.next, type(None))):
            res.next = ListNode(0)
            return self.kuriage(l1.next, l2.next, res.next, n)
        elif not isinstance(l1.next, type(None)):
            res.next = ListNode(0)
            l2.next = ListNode(0)
            return self.kuriage(l1.next, l2.next, res.next, n)
        elif not isinstance(l2.next, type(None)):
            res.next = ListNode(0)
            l1.next = ListNode(0)
            return self.kuriage(l1.next, l2.next, res.next, n)

        if n != 0:
            res.next = ListNode(0)
            res.next.val = n

        return
