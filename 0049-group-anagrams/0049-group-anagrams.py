class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        Q. What if there are duplicates
        Q. What if the element being checked is already in another list (an anagram with two different words) -> In this case, both of them will be in the same list
        """

        if not len(strs):
            return [[""]]
        
        def MapIt(s):
            hashMap = {}
            for i in s:
                if i not in hashMap:
                    hashMap[i] = 1
                else:
                    hashMap[i] += 1
            return hashMap

        listOfHash = []
        returnList = []
        for i in range(len(strs)):
            hashA = MapIt(strs[i])
            if hashA not in listOfHash:
                listOfHash.append(hashA)
                returnList.append([strs[i]])
            else:
                for j in range(len(listOfHash)):
                    if hashA == listOfHash[j]:
                        returnList[j].append(strs[i])
        return returnList


        # for d in list_of_dicts:
        #     if d == your_dict:
        #         print("Found a matching dictionary!")
        #         break  # If you want to stop searching after finding the first match

        # N^2 Time Limit Exceeded
        # returnList = []
        # for i in range(len(strs)):
        #     if not any(strs[i] in sublist for sublist in returnList):
        #         newList = [strs[i]]
        #         hashMapA = MapIt(strs[i])
        #         for j in range(i+1, len(strs)):
        #             hashMapB = MapIt(strs[j])
        #             if hashMapB == hashMapA:
        #                 newList.append(strs[j])
        #         returnList.append(newList)
        # return returnList