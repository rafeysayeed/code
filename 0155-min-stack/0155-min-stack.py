class MinStack(object):
    class Node():
        def __init__(self, val, next, minE):
            self.val = val
            self.next = next
            self.minE = minE

    def __init__(self):
        self.head = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = self.Node(val, None, val)
        else:
            self.head = self.Node(val, self.head, min(self.head.val, val))

    def pop(self):
        """
        :rtype: None
        """
        temp = self.head
        self.head = self.head.next
        temp = None
        

    def top(self):
        """
        :rtype: int
        """
        return self.head.val
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.head.minE


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()