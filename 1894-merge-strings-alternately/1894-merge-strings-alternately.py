class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1, l2, ret = len(word1), len(word2), ""
        for i in range (max(l1, l2)):
            if (i < l1):
                ret += word1[i]
            if (i < l2):
                ret += word2[i]
        return ret