# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is not None:
            current = head
            next = None
            prev = None
            while current != None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            head = prev
        return head
        