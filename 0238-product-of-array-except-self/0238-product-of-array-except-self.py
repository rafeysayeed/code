class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        [a b c d]
        [bcd acd abd abc]
        [a ab abc abcd]
        [abcd bcd cd d]
        [1 a ab abc] - pre
        [bcd cd d 1]
        [bcd acd abd abc]
        """
        # bruteforce O(n^2)
        # answer = []
        # for i in range(len(nums)):
        #     carry = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         carry *= nums[j]
        #     answer += [carry]
        # return answer

        # making prefix
        # pre = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     pre[i] = pre[i-1] * nums[i-1]
        # # making postfix
        # post = [1] * len(nums)
        # for i in range(len(nums)-2, -1, -1):
        #     post[i] = post[i+1] * nums[i+1]
        # # combining
        # answer = []
        # for i in range(len(nums)):
        #     answer += [pre[i]*post[i]]
        # return answer

        answer = [1] * len(nums)
        curr = 1
        for i in range(len(nums)):
            answer[i] *= curr
            curr *= nums[i]
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= curr
            curr *= nums[i]
        return answer