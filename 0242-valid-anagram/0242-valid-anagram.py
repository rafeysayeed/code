class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) != len(t):
        #     return False
        # hashmap1, hashmap2 = {}, {}
        # for i in range(len(s)):
        #     hashmap1[s[i]] = hashmap1.get(s[i], 0) + 1
        #     hashmap2[t[i]] = hashmap2.get(t[i], 0) + 1
        # if hashmap1 != hashmap2:
        #     return False
        # return True

        # x, y = sorted(s), sorted(t)
        # return x == y

        # hashmap = defaultdict(int)
        # for i in s:
        #     hashmap[i] += 1
        # for i in t:
        #     hashmap[i] -= 1
        # for v in hashmap.values():
        #     if v != 0:
        #         return False
        # return True

        if len(s) != len(t):
            return False
        memo = {}
        for i in s:
            if i not in memo:
                if s.count(i) != t.count(i):
                    return False
                memo[i] = None
        return True