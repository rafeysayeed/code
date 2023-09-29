class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        string = ""
        for i in range(len(address)):
            if address[i] == ".":
                string += "[.]"
            else:
                string += address[i]
        return string

