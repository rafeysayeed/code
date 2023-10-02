class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = list(s)
        left = 0
        right = len(ls)-1
        vowels = "aeiouAEIOU"
        while left < right:
            if ls[left] in vowels:
                while right > left and ls[right] not in vowels:
                    right -= 1
                if right <= left:
                    break
                else:
                    temp = ls[left]
                    ls[left] = ls[right]
                    ls[right] = temp
                    right -= 1
            left += 1
        return "".join(ls)