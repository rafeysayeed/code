class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash1 = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash1.keys():
                return [i, hash1[diff]]
            else:                
                hash1[nums[i]] = i