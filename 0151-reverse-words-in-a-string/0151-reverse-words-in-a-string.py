class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s.reverse()
        new_s = ""
        for i in s:
            new_s += i
            new_s += " "
        new_s = new_s.strip()
        return new_s
        # ↑ 12m 50s ↑
