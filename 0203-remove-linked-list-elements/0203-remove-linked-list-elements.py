# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        temp = prev = head
        while temp:
            if temp.val == val:
                if prev == temp:
                    head = prev = temp = temp.next
                else:
                    prev.next = temp.next
                    temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return head