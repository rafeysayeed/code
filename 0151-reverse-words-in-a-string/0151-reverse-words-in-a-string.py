class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        newStr = ""
        tick = len(s) - 1
        while tick > -1:
            if s[tick] != " ":
                end = tick + 1
                while tick > -1 and s[tick] != " ":
                    tick -= 1
                newStr += s[tick+1:end]
                newStr += " "
            else:
                tick -= 1
        return newStr.strip(" ")