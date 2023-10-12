class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        retList = []
        total = target
        def recurse(candidates, total, temp, i):
            # print(temp, i, total)
            total -= i
            temp = temp[:]
            temp += [i]
            if total < 0:
                if temp:
                    temp.pop()
                return
            if total == 0:
                retList.append(temp)
                return
            for k in range(len(candidates)):
                recurse(candidates, total, temp, candidates[k])
                
        for i in range(len(candidates)):
            recurse(candidates, target, [], candidates[i])
        # print(retList)

        newList = []
        for i in retList:
            if sorted(i) not in newList:
                newList.append(sorted(i))
        return newList