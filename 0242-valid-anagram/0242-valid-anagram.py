class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s, t = sorted(s), sorted(t)
        return s == t
        # if len(s) != len(t):
        #     return False
        # hash1, hash2 = {}, {}
        # for i in range(len(s)):
        #     if s[i] not in hash1:
        #         hash1[s[i]] = 1
        #     else:
        #         hash1[s[i]] += 1
        #     if t[i] not in hash2:
        #         hash2[t[i]] = 1
        #     else:
        #         hash2[t[i]] += 1
        # return hash1 == hash2