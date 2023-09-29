class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        # Copied
        x = 0
        for i in operations:
            if i[1] == "-":
                x -= 1
            else:
                x += 1
        return x

        # My solution
        # x = 0
        # for i in operations:
        #     if i[0] == "X":
        #         if i[1:] == "--":
        #             x -= 1
        #         else:
        #             x += 1
        #     else:
        #         if i[0:2] == "--":
        #             x -= 1
        #         else:
        #             x += 1
        # return x