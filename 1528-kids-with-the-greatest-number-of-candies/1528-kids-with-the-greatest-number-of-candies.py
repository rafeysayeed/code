class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ret = []
        maximus = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximus:
                ret.append(True)
            else:
                ret.append(False)
        return ret