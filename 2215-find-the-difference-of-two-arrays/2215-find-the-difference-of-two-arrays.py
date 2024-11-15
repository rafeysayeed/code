class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1, set2 = set(nums1), set(nums2)
        l1,l2=[],[]
        for i in set1:
            if i in set2:
                continue
            l1 += [i]
        for i in set2:
            if i in set1:
                continue
            l2 += [i]
        return [l1, l2]
