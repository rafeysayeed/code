class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        i = 0
        while i < len(s):
            if (s[i] == "}"):
                b = stack.pop()
                if b != "{":
                    return False
            elif (s[i] == "]"):
                b = stack.pop()
                if b != "[":
                    return False
            elif (s[i] == ")"):
                b = stack.pop()
                if b != "(":
                    return False
            else:
                stack.append(s[i])
            i += 1
        return True if len(stack) == 0 else False