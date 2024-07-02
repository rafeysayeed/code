class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 1
        total = 0
        while j < len(s):
            total += abs(ord(s[i]) - ord(s[j]))
            i += 1
            j += 1
        return total