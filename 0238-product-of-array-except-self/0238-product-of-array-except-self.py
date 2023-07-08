class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ret = []
        # for i in range(len(nums)):
        #     multiply = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         else:
        #             multiply *= nums[j]
        #     ret.append(multiply)

        # return ret

        ret = []
        fix = 1
        for i in range(len(nums)):
            ret.append(fix)
            fix *= nums[i]
        fix = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= fix
            fix *= nums[i]
        return ret
                