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

        """
            2 + 5 = 7
            4 + 6 = 10 = 0
            3 + 4 = 7 + 1 = 8

            9 + 9 = 18 = 8
            9 + 9 = 18 + 1 = 19 = 9
            9 + 9 = 18 + 1 = 19 = 9
            9 + 9 = 18 + 1 = 19 = 9
            9 + 0 = 9 + 1 = 10 = 0
            9 + 0 = 9 + 1 = 10 = 0
            9 + 0 = 9 + 1 = 10 = 0
            0 + 0 = 0 + 1 = 1

            1 0 0 0 9 9 9 8

            addition
            extraction of carry
            restoration of units place
            adding carry to next result
            addition of new index
        """

        # approach 1: 18m
        # digit1, digit2 = [], []
        # temp1, temp2 = l1, l2
        # while temp1 != None:
        #     digit1.append(temp1.val)
        #     temp1 = temp1.next
        # while temp2 != None:
        #     digit2.append(temp2.val)
        #     temp2 = temp2.next
        # number1, number2 = 0, 0
        # tenPo = 1
        # for i in digit1:
        #     number1 += i * tenPo
        #     tenPo *= 10
        # tenPo = 1
        # for i in digit2:
        #     number2 += i * tenPo
        #     tenPo *= 10
        # result = number1 + number2
        # tenPo = 10
        # resultNode = None
        # curr = None
        # while result > 0:
        #     catch = result % tenPo
        #     result //= tenPo
        #     if not resultNode:
        #         resultNode = ListNode(catch)
        #         curr = resultNode
        #     else:
        #         curr.next = ListNode(catch)
        #         curr = curr.next
        # return resultNode if resultNode else ListNode(0)

        # approach 2:
        temp1, temp2 = l1, l2
        carry = 0
        tenPo = 1
        resultNode, curr = None, None
        while temp1 or temp2 or carry:
            if temp1 and temp2:
                A = temp1.val
                B = temp2.val
                temp1 = temp1.next
                temp2 = temp2.next
            elif temp1:
                A = temp1.val
                B = 0
                temp1 = temp1.next
            elif temp2:
                A = 0
                B = temp2.val
                temp2 = temp2.next
            else:
                A = 0
                B = 0
            C = A + B + carry
            if C > 9:
                carry = 1
                C %= 10
            else:
                carry = 0
            if not resultNode:
                resultNode = ListNode(C)
                curr = resultNode
            else:
                curr.next = ListNode(C)
                curr = curr.next
        return resultNode 