class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max_area = 0
        # for i in range(0, len(height)):
        #     for j in range(i+1, len(height)):
        #         x = j-i
        #         y = min(height[i], height[j])
        #         if max_area < x*y:
        #             max_area = x*y
        # return max_area

        max_area = 0
        left = 0
        right = len(height) - 1
        while left != right:
            x = right - left
            y = min(height[left], height[right])
            if max_area < x * y:
                max_area = x * y
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_area