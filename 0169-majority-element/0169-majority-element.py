class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        goal = len(nums) // 2
        count = 0
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        for k, v in hashMap.items():
            print(k, v)
            if v > goal:
                return k
        