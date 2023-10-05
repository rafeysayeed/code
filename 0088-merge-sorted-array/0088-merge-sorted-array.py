class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # two pointers
        i = m-1
        j = n-1
        k = m+n-1
        while(j >= 0):
            if (i >= 0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        # using in-built sort
        # for i in range(n):
        #     nums1[m+i] = nums2[i]
        # return nums1.sort()