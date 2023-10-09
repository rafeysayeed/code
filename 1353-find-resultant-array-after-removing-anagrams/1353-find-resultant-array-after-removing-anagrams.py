class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) <= 1:
            return words

        A = 0
        B = 1
        while B < len(words):
            wordA = ''.join(sorted(words[A]))
            wordB = ''.join(sorted(words[B]))
            if wordA == wordB:
                words.pop(B)
            else:
                A += 1
                B += 1
        return words