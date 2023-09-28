class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        left = 0
        right = n
        newArr = []
        while right < 2*n:
            newArr.append(nums[left])
            newArr.append(nums[right])
            left += 1
            right += 1
        return newArr