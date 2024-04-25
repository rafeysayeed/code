class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        listS = s.split()
        hashMap = {}
        for i in range(len(pattern)):
            if pattern[i] in hashMap.keys():
                if hashMap[pattern[i]] == listS[i]:
                    continue
                else:
                    return False
            elif listS[i] in hashMap.values():
                return False
            else:
                hashMap[pattern[i]] = listS[i]
            print(i, pattern[i], hashMap[pattern[i]])
        return True