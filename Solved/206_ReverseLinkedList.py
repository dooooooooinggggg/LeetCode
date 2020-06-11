# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    def reverseList(self, head: ListNode):
        if head == None:
            return head

        tmp_first = head
        values = []

        while(1):
            values.insert(0, tmp_first.val)
            if tmp_first.next == None:
                break
            tmp_first = tmp_first.next

        print(values)

        r = head
        i = 0
        while(1):
            r.val = values[i]
            if r.next == None:
                break

            i += 1
            r = r.next

        return head
