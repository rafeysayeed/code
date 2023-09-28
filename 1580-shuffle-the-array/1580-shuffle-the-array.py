class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        newArr = []
        for i in range(n):
            newArr.append(nums[i])
            newArr.append(nums[i+n])
        return newArr