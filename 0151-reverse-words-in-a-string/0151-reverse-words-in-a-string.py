class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        stack = []
        retStr = ""
        i = 0
        while i < len(s):
            word = ""
            while i < len(s) and s[i] != " ":
                word += s[i]
                i += 1
            stack.append(word)
            i += 1
        while stack:
            word = stack.pop(-1)
            if not word:
                continue
            retStr += word + " "
        return retStr.strip()