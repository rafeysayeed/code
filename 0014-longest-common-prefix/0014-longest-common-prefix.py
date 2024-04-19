class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        while i < min(len(first), len(last)) and first[i] == last[i]:
            ans += first[i]
            i += 1
        return ans

