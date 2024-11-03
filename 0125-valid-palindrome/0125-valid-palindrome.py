class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re

        def rm(s):
            return re.sub(r'[^a-zA-Z0-9]', '', s)
        s = rm(s)
        s = s.lower()
        
        return s == s[::-1]