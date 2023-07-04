class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        map_hash = {}
        for i in arr:
            if i in map_hash:
                map_hash[i] += 1
            else:
                map_hash[i] = 1
        values = list(map_hash.values())
        if len(values) != len(set(values)):
            return False
        else:
            return True