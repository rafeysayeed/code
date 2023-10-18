class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,1,1] -> [1]
        """
        seen = []
        for i in nums:
            if i not in seen:
                seen += [i]
        for i in range(len(seen)):
            nums[i] = seen[i]
        return len(seen)