class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if (nums[i] == val):
                j = i + 1
                if (j < len(nums)):
                    while ((j < len(nums)) and (nums[j] == nums[i])): 
                        j += 1
                if j < len(nums) and (nums[j] != nums[i]): # case: when val == val, don't run
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp 
                    count += 1
            else:
                count += 1
        return count
