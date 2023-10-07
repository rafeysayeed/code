class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        hashMap1 = {}
        for i in range(len(s)):
            if s[i] not in hashMap1:
                hashMap1[s[i]] = t[i]
            else:
                if t[i] == hashMap1[s[i]]:
                    continue
                else:
                    return False
        hashMap2 = {}
        for i in range(len(t)):
            if t[i] not in hashMap2:
                hashMap2[t[i]] = s[i]
            else:
                if s[i] == hashMap2[t[i]]:
                    continue
                else:
                    return False
        return True

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