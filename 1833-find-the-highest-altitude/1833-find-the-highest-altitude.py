class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxima = 0
        max_alt = 0
        for i in range(len(gain)):
            max_alt += gain[i]
            if max_alt > maxima:
                maxima = max_alt
        return maxima