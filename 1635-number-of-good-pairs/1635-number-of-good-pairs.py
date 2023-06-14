class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] == nums[j]):
        #             count += 1
        # return count

        dojo = {}
        counter = 0
        for i in nums:
            friend_count = dojo.get(i,0)
            counter += friend_count
            dojo[i] = friend_count + 1
        return counter