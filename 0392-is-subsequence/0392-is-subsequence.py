class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(t):
            if j < len(s) and t[i] == s[j]:
                j += 1
            i += 1
        return j == len(s)