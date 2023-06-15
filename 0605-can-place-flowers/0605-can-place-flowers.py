class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        [1,0,0,0,1]
        [0,1,0,1,0]
        [0,0,1]
        [1,0,1,0,1,0,0,0,1]
        [1,0,1,0,0,1,0,0]
        [0]
        [0,0]
        [0,0,1,0,0]
        """
        # for i in range(len(flowerbed)):
        #     if (flowerbed[i] == 0):
        #         if (i-1 < 0):
        #             if (i+1 == len(flowerbed)):
        #                 flowerbed[i] = 1
        #                 n -= 1
        #             elif (flowerbed[i+1] != 1):
        #                 flowerbed[i] = 1
        #                 n -= 1
        #         elif (i == len(flowerbed)-1):
        #             if (flowerbed[i-1] != 1):
        #                 flowerbed[i] = 1
        #                 n -= 1
        #         elif (flowerbed[i-1] != 1):
        #             if (flowerbed[i+1] != 1):
        #                 flowerbed[i] = 1
        #                 n -= 1
        #     print(n)
        # if n <= 0: # can ask for planting less than available spots, n can be < 0
        #     return True
        # return False

        f = [0] + flowerbed + [0]
        for i in range(1, len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0
