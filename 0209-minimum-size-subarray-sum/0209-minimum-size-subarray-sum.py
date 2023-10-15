class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        [0,1,2,3,4,5]
        [2,3,1,2,4,3]
        target = 7
        left = 5
        total = 3
        right = 6
        count = 2
        diff = 5 - 4 + 1 = 2
        """
        left, total = 0, 0
        count = len(nums)+1
        for right in range(len(nums)):
            total += nums[right]
            if total >= target:
                while total >= target:
                    diff = right - left + 1
                    count = diff if diff < count else count
                    total -= nums[left]
                    left += 1
        return 0 if count == len(nums)+1 else count