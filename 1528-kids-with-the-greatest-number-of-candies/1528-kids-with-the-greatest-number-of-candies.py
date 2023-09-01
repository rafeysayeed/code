class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        retrun = []
        max_candies = max(candies)
        for i in candies:
            if i + extraCandies >= max_candies:
                retrun.append(True)
            else:
                retrun.append(False)
        return retrun