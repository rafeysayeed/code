class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        same length len(s) == len(t)
        same characters 
        """
        sortedT = ''.join(sorted(t))
        sortedS = ''.join(sorted(s))
        return sortedS == sortedT