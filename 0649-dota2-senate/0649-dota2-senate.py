class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        RDDDRDRRDR
        DDRRR
        """
        r, d = [], []
        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
        while len(r) and len(d):   
            a, b = r.pop(0), d.pop(0)
            if a < b:
                r.append(b+2)
            else:
                d.append(a+2)
        if len(r) == 0:
            return "Dire"
        else:
            return "Radiant"