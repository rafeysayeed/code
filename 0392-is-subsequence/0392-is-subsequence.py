class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls, lt = len(s), len(t)
        ptr = 0
        if ls and not lt:
                return False
        elif not ls:
                return True
        for i in range(lt):
            if t[i] == s[ptr]:
                ptr += 1
            if ptr == ls:
                return True
        return False