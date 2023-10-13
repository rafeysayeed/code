class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        A = 0
        B = 0
        while A < len(s) and B < len(t):
            if s[A] == t[B]:
                A += 1
                B += 1
            else:
                B += 1
        return A == len(s)