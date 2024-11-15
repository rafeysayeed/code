class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1,p2=0,1
        while p1 < len(nums) and p2 < len(nums):
            if nums[p1] == 0:
                while p2 < len(nums) and nums[p2] == 0:
                    p2 += 1
                if p2 < len(nums):
                    nums[p1] = nums[p2]
                    nums[p2] = 0
            p1 += 1