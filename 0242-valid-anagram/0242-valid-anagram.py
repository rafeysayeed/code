class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hashmap1, hashmap2 = {}, {}
        for i in range(len(s)):
            hashmap1[s[i]] = hashmap1.get(s[i], 0) + 1
            hashmap2[t[i]] = hashmap2.get(t[i], 0) + 1
        if hashmap1 != hashmap2:
            return False
        return True