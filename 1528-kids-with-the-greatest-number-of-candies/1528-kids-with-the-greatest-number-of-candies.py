class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ret = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                ret.append(True)
            else:
                ret.append(False)
        return ret