class MinStack(object):

    def __init__(self):
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.min_stack:
            self.min_stack.append([val,val])
            return
        min_ele = self.min_stack[-1][1]
        self.min_stack.append([val,min(val,min_ele)])

    def pop(self):
        """
        :rtype: None
        """
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.min_stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()