class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # i = 0
        # while i < len(s):
        #     if (s[i] == "*"):
        #         if i+1 < len(s) and s[i+1] == "*":
        #             s = s[:i-1] + s[i+1:]
        #             i -= 1
        #         else:
        #             s = s[:i-1] + s[i+1:]
        #     else:
        #         i += 1
        # return s

        stack = []
        for i in range(len(s)):
            if s[i] != "*":
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)