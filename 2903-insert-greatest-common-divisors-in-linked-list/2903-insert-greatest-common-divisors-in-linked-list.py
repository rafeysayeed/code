# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def getGCD(a, b):
            gcd = 0
            for i in range(1, min(a,b)+1):
                if a % i == 0 and b % i == 0:
                        gcd = i
            return gcd
        
        temp = head
        while temp:
            if not temp.next:
                break
            a = temp.val
            b = temp.next.val
            c = getGCD(a, b)
            temp2 = temp.next
            temp.next = ListNode(c)
            temp.next.next = temp2
            temp = temp.next.next
        return head