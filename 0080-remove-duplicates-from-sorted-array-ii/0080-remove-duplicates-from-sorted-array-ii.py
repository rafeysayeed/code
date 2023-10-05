class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        print(nums)
        nums[2:] = nums[3:]
        print(nums)
        case 1 : check if it responds to array resizing
        test cases
        [0,0,1]
        """

        i = 0
        while i < len(nums):
            print(nums)
            currentElement = nums[i]
            count = 0
            while i < len(nums) and nums[i] == currentElement:
                count += 1
                i += 1
            if count > 2:
                checkpoint = i
                i = i - count + 2
                nums[i:] = nums[checkpoint:]
            # print(nums, count, checkpoint, i)

        # i = 0
        # k = 0
        # while i < len(nums):
        #     print(nums)
        #     count = 0
        #     if i < len(nums)-1 and nums[i] == nums[i+1]:
        #         i += 1
        #         count += 1
        #     if count >= 2:
        #         check = i
        #         i -= count + 2
        #         nums[i:] = nums[check+1:]
        #     else:
        #         i += 1            