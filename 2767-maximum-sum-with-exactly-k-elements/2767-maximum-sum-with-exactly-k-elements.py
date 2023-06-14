class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        while k > 0:
            m = max(nums)
            i = nums.index(m)
            nums[i] = m + 1
            sum += m
            k -= 1
        return sum