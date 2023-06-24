class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ret = []
        for i in range(len(candies)):
            t = candies[i]
            candies[i] += extraCandies
            if candies[i] >= max(candies):
                ret.append(True)
            else:
                ret.append(False)
            candies[i] = t
        return ret