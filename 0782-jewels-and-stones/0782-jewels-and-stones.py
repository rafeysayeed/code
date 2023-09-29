class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = {}
        returnCount = 0
        for i in stones:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for i in jewels:
            if i in count:
                returnCount += count[i]
        return returnCount