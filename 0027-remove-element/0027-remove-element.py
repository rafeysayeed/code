class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)
        #     i += 1
        # return len(nums)

        # edge cases: [], [1]val=1->[], [3,3]val=3->[], [2,2]val=1, [2]val=1
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left < len(nums) and nums[left] != val:
                left += 1
            while right >= 0 and nums[right] == val:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return left if len(nums) else 0