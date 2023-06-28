class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Sliding window will not work when k = 32483 (Time Limit Exceeds)
        # maxima = None
        # for i in range(len(nums)):
        #     if i + k - 1 < len(nums):
        #         val = sum(nums[i:i+k])
        #         if maxima == None or val > maxima:
        #             maxima = float(val)
        #     else:
        #         break
        # return maxima / k

        mid = sum(nums[0:k])
        maxima = float(mid)
        for i in range(len(nums)-k):
            mid += nums[i+k] - nums[i]
            maxima = float(max(maxima, mid))
        return maxima/k