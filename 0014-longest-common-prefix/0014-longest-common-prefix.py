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
        mint = min(len(first), len(last))
        while i < mint and first[i] == last[i]:
            ans += first[i]
            i += 1
        return ans

