class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [0] * (len(nums) * 2)
        for i in range(len(nums)):
            ret[i] = nums[i]
            ret[len(nums)+i] = nums[i]
        return ret