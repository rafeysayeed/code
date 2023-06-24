class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        point = 2
        i = 2
        [1,0,1,0,1]
        [0,1,0,3,12]
        [1,1,0]
        """
        point = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if point != i:
                    nums[point] = nums[i]
                    nums[i] = 0
                    point += 1
                else:
                    point += 1