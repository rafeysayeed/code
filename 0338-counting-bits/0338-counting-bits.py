class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ls = []
        for i in range(n+1):
            bit = 0
            while (i > 0):
                bit += i % 2
                i /= 2
            ls.append(bit)
        return ls
            