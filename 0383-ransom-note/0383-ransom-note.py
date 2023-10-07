class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashMap = {}
        for i in magazine:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        for i in ransomNote:
            if i in hashMap and hashMap[i] > 0:
                hashMap[i] -= 1
            else:
                return False
        return True

        # hashMap1, hashMap2 = {}, {}
        # for i in magazine:
        #     if i not in hashMap1:
        #         hashMap1[i] = 1
        #     else:
        #         hashMap1[i] += 1
        # for i in ransomNote:
        #     if i not in hashMap2:
        #         hashMap2[i] = 1
        #     else:
        #         hashMap2[i] += 1
        # for k, v in hashMap2.items():
        #     if k in hashMap1 and v <= hashMap1[k]:
        #         continue
        #     else:
        #         return False
        # return True