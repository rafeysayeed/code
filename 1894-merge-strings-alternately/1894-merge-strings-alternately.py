class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        # # My Solution
        # ret = ""
        # ptr1 = ptr2 = 0
        # while ptr1 < len(word1) or ptr2 < len(word2):
        #     if ptr1 < len(word1):
        #         ret += word1[ptr1]
        #         ptr1 += 1
        #     if ptr2 < len(word2):
        #         ret += word2[ptr2]
        #         ptr2 += 1
        # return ret
        
        # Another Solution: Use single counter
        ret = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                ret += word1[i]
            if i < len(word2):
                ret += word2[i]
            i += 1
        return ret