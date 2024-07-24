class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        hash1, hash2 = {}, {}
        for i in word1:
            # hash1[i] = hash1.get(0, hash1[i] + 1)
            hash1[i] = hash1.get(i, 0) + 1
        for i in word2:
            hash2[i] = hash2.get(i, 0) + 1

        k1 = hash1.keys()
        k1.sort()
        k2 = hash2.keys()
        k2.sort()
        k1 = str(k1)
        k2 = str(k2)

        v1 = hash1.values()
        v1.sort()
        v2 = hash2.values()
        v2.sort()

        return v1 == v2 and k1 == k2
        