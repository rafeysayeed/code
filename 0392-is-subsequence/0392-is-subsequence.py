class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j=0,0
        ns,nt=len(s),len(t)
        if ns==0:
            return True
        elif nt==0 and ns:
            return False
        while j<nt:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i==ns