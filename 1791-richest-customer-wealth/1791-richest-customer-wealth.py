class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for i in accounts:
            amount = 0
            for j in i:
                amount += j
            if amount > richest:
                richest = amount
        return richest