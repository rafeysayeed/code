class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashm = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashm:
                return [hashm[diff], i]
            else:
                hashm[nums[i]] = i