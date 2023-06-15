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
        [0.0]
        """
        # for i in range(len(flowerbed)):
        #     if flowerbed[i] == 1:
        #         if i+2 < len(flowerbed) and flowerbed[i+2] == 0:
        #             if i+2 == len(flowerbed) - 1:
        #                     n -= 1
        #                     flowerbed[i+2] = 1
        #             elif i+3 < len(flowerbed) and flowerbed[i+3] == 0:
        #                 n -= 1
        #                 flowerbed[i+2] = 1
        #     elif flowerbed[i] == 0:
        #         if i == 0:
        #             if i < len(flowerbed) - 1 and flowerbed[i+1] == 0:
        #                 n -= 1
        #                 flowerbed[i] = 1
        #         elif i-1 > 0 and flowerbed[i-1] != 1:
        #             if i < len(flowerbed) and flowerbed[i+1] == 0:
        #                 n -= 1
        #                 flowerbed[i] = 1
        # if n == 0:
        #     return True
        # return False
        # # [1,0,1,0,1,0,0]
        for i in range(len(flowerbed)):
            #print(flowerbed)
            if (flowerbed[i] == 0):
                if (i-1 < 0):
                    if (i+1 == len(flowerbed)):
                        flowerbed[i] = 1
                        n -= 1
                    elif (flowerbed[i+1] != 1):
                        flowerbed[i] = 1
                        n -= 1
                elif (i == len(flowerbed)-1):
                    if (flowerbed[i-1] != 1):
                        #print("chala")
                        flowerbed[i] = 1
                        n -= 1
                elif (flowerbed[i-1] != 1):
                    if (flowerbed[i+1] != 1):
                        flowerbed[i] = 1
                        n -= 1
        if n <= 0:
            return True
        return False
