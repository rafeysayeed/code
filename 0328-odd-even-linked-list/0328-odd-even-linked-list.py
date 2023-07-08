# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # edge case: empty list, 1 element, odd element, even elements
        if not head or not head.next:
            return head
    
        odd = ListNode()
        odd = head
        even = ListNode()
        even = head.next
        evenStart = ListNode()
        evenStart = head.next

        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenStart
        if not odd.next:
            even.next = None
        
        return head
