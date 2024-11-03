class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {} # hashmap
        for i in range(len(numbers)):
            a = target - numbers[i]
            # b = target - a
            if a in h:
                return [h[a]+1, i+1]
            else:
                h[numbers[i]] = i
        