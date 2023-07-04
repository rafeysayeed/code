class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maximus = float(sum(nums[:k]))
        summa = maximus
        for i in range(len(nums)-k):
            summa = summa - nums[i] + nums[k+i] #sum(nums[i+1:k+i+1])
            if summa > maximus:
                maximus = float(summa)
        return float(maximus / k)
