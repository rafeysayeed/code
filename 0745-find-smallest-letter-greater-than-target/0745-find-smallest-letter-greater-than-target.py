class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        smallest = letters[0]
        for i in letters:
            if ord(i) > ord(target):
                smallest = i
                break
        return smallest
        