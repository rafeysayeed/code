class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        new = heights[:]
        new.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != new[i]:
                count += 1
        return count