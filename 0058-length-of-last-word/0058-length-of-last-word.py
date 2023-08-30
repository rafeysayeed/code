class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while i > -1  and s[i] == " ":
            i -= 1
        start = i
        while i > -1 and s[i] != " ":
            i -= 1
        stop = i
        return start - stop