class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = len(word1)
        l2 = len(word2)
        c1 = 0
        c2 = 0
        merged = ""
        while c1 != l1 or c2 != l2:
            if c1 < l1:
                merged += word1[c1]
                c1 += 1
            if c2 < l2:
                merged += word2[c2]
                c2 += 1
        return merged