class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,1,1] -> [1]
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]: # ← indicates unique element
                i += 1
                nums[i] = nums[j]
        return i + 1


        # # My Sol
        # seen = []
        # for i in nums:
        #     if i not in seen:
        #         seen += [i]
        # for i in range(len(seen)):
        #     nums[i] = seen[i]
        # return len(seen)