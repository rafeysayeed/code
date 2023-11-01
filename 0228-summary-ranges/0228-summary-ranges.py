class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def Decorator(_intervals):
            strList = []
            for i in _intervals:
                if i[0] == i[1]:
                    temp = str(i[0])
                    strList.append(temp)
                else:
                    temp = str(i[0]) + "->" + str(i[1])
                    strList.append(temp)
            return strList
        
        intervals = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i+1] == nums[i]+1:
                i += 1
            end = nums[i]
            intervals.append([start, end])
            i += 1
        return Decorator(intervals)
