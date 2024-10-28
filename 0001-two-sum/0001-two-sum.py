class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        target = a + b
        a = target - b
        b = target - a
        target = (target - b) + (target - a)
        """
        n = nums
        t = target
        d = 0 # difference
        hd = {}
        for i in range(len(n)):
            d = t - n[i]
            b = t - d
            if b in hd:
                return [i, hd[b]]
            else:
                hd[d] = i
