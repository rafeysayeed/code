class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        while i < len(nums):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j+=1
            i += 1