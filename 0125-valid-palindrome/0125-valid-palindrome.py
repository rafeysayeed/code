class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(lambda x: x.isalpha() or x.isdigit(), s)).lower()
        return s == s[::-1]