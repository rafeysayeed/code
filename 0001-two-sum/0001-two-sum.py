class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # bruteforce
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # hash map
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        # This approach is not correct because it will change the indexes to return
        # nums = sorted(nums)
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     sum = nums[left] + nums[right]
        #     if sum == target:
        #         return [left, right]
        #     elif sum > target:
        #         right -= 1
        #     else:
        #         left += 1