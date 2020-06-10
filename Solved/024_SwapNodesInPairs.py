# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # def swapPairs(self, head: ListNode) -> ListNode:
    def swapPairs(self, head: ListNode):
        if head == None:
            return head

        tmp = head
        while(1):
            now = tmp
            if now.next == None:
                break
            self.swapTwo(now)
            if now.next.next == None:
                break
            tmp = tmp.next.next
        return head

    def swapTwo(self, now):
        val_1 = now.next.val
        val_2 = now.val
        now.val = val_1
        now.next.val = val_2

    def printList(self, l):
        tmp = l
        while(1):
            print(tmp.val)
            if tmp.next == None:
                break
            tmp = tmp.next

        print("-------")
