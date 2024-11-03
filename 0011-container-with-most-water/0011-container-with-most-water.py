class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, b, mw = 0, 0, 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         l = min(height[i], height[j])
        #         b = j - i
        #         mw = max(mw, l*b)
        le, r = 0, len(height)-1
        while le < r:
            l = min(height[le], height[r])
            b = r - le
            mw = max(mw, l*b)
            if height[le] < height[r]:
                le += 1
            else:
                r -= 1
        return mw