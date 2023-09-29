class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        returnString = ""
        for i in range(len(command)):
            if command[i] == "G":
                returnString += "G"
            elif command[i] == "(":
                if command[i+1] == "a":
                    returnString += "al"
                    i += 4
                else:
                    returnString += "o"
                    i += 2
        return returnString