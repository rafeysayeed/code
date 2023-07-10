# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # list1 = []
        # list2 = []
        # while l1 is not None:
        #     list1.append(l1.val)
        #     l1 = l1.next
        # while l2 is not None:
        #     list2.append(l2.val)
        #     l2 = l2.next
        # list1 = list1[::-1]
        # list2 = list2[::-1]
        
        # print(list1, list2)

        n1, n2, r = [], [], []
        t1 = ListNode()
        t2 = ListNode()
        t1, t2 = l1, l2
        while t1 is not None:
            n1.append(t1.val)
            t1 = t1.next
        while t2 is not None:
            n2.append(t2.val)
            t2 = t2.next
        carry = 0
        while len(n1) or len(n2):
            a1, a2 = 0, 0
            if len(n1):
                a1 = n1.pop(0)
            if len(n2):
                a2 = n2.pop(0)
            a1 += a2 + carry
            carry = a1 // 10
            not_carry = a1 % 10
            r.append(not_carry)
        if carry:
            r.append(carry)
        ret = ListNode()
        ret.val = r[0]
        temp = ListNode()
        temp = ret
        for i in range(1, len(r)):
            newnode = ListNode()
            newnode.val = r[i]
            temp.next = newnode
            temp = temp.next
        return ret