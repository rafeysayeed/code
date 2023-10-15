class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        refinedString = ""
        for i in s:
            if i.isalnum():
                refinedString += i.lower()
        return refinedString == refinedString[::-1]