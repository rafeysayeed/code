class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,1,1] -> [1]
        """
        arr = []
        i = 1
        while (i < len(nums)):
            if nums[i] == nums[i-1]:
                arr += [nums.pop(i)]
            else:
                i += 1
        k = len(nums)
        for i in range(len(arr)):
            nums += [arr[i]]
        return k
            

        # i = 0
        # for j in range(1, len(nums)):
        #     if nums[i] != nums[j]: # ← indicates unique element
        #         i += 1
        #         nums[i] = nums[j]
        # return i + 1


        # # My Sol
        # seen = []
        # for i in nums:
        #     if i not in seen:
        #         seen += [i]
        # for i in range(len(seen)):
        #     nums[i] = seen[i]
        # return len(seen)

        # i = 1
        # while i < len(nums):
        #     if nums[i-1] == nums[i]:
        #         to_replace = (i, nums[i])
        #         while i < len(nums) and nums[i] == to_replace[1]:
        #             i += 1
        #         if i < len(nums):
        #             nums[to_replace[0]] = nums[i]
        #             i = to_replace[0] + 1
        #     else:
        #         i += 1
        # return to_replace[0] + 1