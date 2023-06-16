class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ret = ""
        ptr1 = ptr2 = 0
        while ptr1 < len(word1) or ptr2 < len(word2):
            if ptr1 < len(word1):
                ret += word1[ptr1]
                ptr1 += 1
            if ptr2 < len(word2):
                ret += word2[ptr2]
                ptr2 += 1
        return ret