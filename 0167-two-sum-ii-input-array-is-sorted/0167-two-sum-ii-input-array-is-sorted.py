class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        i = 0
        while i < len(numbers):
            diff = target - numbers[i]
            if diff in hashMap.keys():
                return [hashMap[diff]+1, i+1]
            else:
                hashMap[numbers[i]] = i
            i += 1
        return []