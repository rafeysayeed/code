class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ret = []
        maxima = max(candies)
        for i in range(len(candies)):
            # t = candies[i]
            # candies[i] += extraCandies # no need to use extra memory and steps
            # if candies[i] >= max(candies): # no need to calculate at every iteration
            if candies[i] + extraCandies >= maxima:
                ret.append(True)
            else:
                ret.append(False)
            # candies[i] = t
        return ret