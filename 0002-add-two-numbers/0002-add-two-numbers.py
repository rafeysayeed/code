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
        # # Draft 1
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

        # # Draft 2
        # n1, n2, r = [], [], []
        # t1 = ListNode()
        # t2 = ListNode()
        # t1, t2 = l1, l2
        # while t1 is not None:
        #     n1.append(t1.val)
        #     t1 = t1.next
        # while t2 is not None:
        #     n2.append(t2.val)
        #     t2 = t2.next
        # carry = 0
        # while len(n1) or len(n2):
        #     a1, a2 = 0, 0
        #     if len(n1):
        #         a1 = n1.pop(0)
        #     if len(n2):
        #         a2 = n2.pop(0)
        #     a1 += a2 + carry
        #     carry = a1 // 10
        #     not_carry = a1 % 10
        #     r.append(not_carry)
        # if carry:
        #     r.append(carry)
        # ret = ListNode()
        # ret.val = r[0]
        # temp = ListNode()
        # temp = ret
        # for i in range(1, len(r)):
        #     newnode = ListNode()
        #     newnode.val = r[i]
        #     temp.next = newnode
        #     temp = temp.next
        # return ret

        # # NeetCode
        # dummy = ListNode()
        # cur = dummy
        # carry = 0
        # while l1 or l2 or carry:
        #     v1 = l1.val if l1 else 0
        #     v2 = l2.val if l2 else 0
        #     val = v1 + v2 + carry
        #     carry = val // 10
        #     val = val % 10
        #     cur.next = ListNode(val)
        #     cur = cur.next
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        # return dummy

        # Strings
        # treat them as string and reverse them
        s1 = ""
        cur = l1
        while cur:
            s1 += str(cur.val)
            cur = cur.next

        s2 = ""
        cur = l2
        while cur:
            s2 += str(cur.val)
            cur = cur.next

        s1 = s1[::-1]
        s2 = s2[::-1]

        # Calculate the new number
        res_string = str(int(s1) + int(s2))
        
        # Reverse it
        res_string = res_string[::-1]

        # Create the new LinkedList
        dummy = ListNode(-1)

        prev = dummy
        for char in res_string:
            cur = ListNode(int(char))
            prev.next = cur

            prev = cur

        return dummy.next
        