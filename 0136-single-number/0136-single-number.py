class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bit manipulation
        res = 0
        for i in nums:
            res ^= i
        return res