class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # NeetCode
        hash1, hash2 = {}, {}
        for c1, c2 in zip(s, t):
            if ((c1 in hash1 and hash1[c1] != c2) or
            (c2 in hash2 and hash2[c2] != c1)):
                return False
            hash1[c1] = c2
            hash2[c2] = c1
        return True

        # Intuition 2
        # hashMap1 = {}
        # for i in range(len(s)):
        #     if s[i] not in hashMap1:
        #         hashMap1[s[i]] = t[i]
        #     else:
        #         if t[i] == hashMap1[s[i]]:
        #             continue
        #         else:
        #             return False
        # hashMap2 = {}
        # for i in range(len(t)):
        #     if t[i] not in hashMap2:
        #         hashMap2[t[i]] = s[i]
        #     else:
        #         if s[i] == hashMap2[t[i]]:
        #             continue
        #         else:
        #             return False
        # return True

        # Intuition 1
        # if len(s) != len(t):
        #     return False

        # hashMap1, hashMap2 = {}, {}
        # for i in range(len(s)):
        #     if s[i] not in hashMap1:
        #         hashMap1[s[i]] = [i]
        #     else:
        #         hashMap1[s[i]] += [i]
        #     if t[i] not in hashMap2:
        #         hashMap2[t[i]] = [i]
        #     else:
        #         hashMap2[t[i]] += [i]

        # for k, v in hashMap1.items():
        #     if v in hashMap2.values():
        #         continue
        #     else:
        #         return False
        # return True