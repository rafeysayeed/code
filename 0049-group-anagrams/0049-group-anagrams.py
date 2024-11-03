class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in strs:
            sw = "".join(sorted(i))
            if sw in d:
                d[sw] += [i]
            else:
                d[sw] = [i]
        ll = []
        for _, i in d.items():
            ll += [i]
        return ll