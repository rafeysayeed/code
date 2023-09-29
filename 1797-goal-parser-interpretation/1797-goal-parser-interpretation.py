class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace("()", "o").replace("(al)", "al")
        # returnString = ""
        # for i in range(len(command)):
        #     if command[i] == "G":
        #         returnString += "G"
        #     elif command[i] == "(":
        #         if command[i+1] == "a":
        #             returnString += "al"
        #             i += 4
        #         else:
        #             returnString += "o"
        #             i += 2
        # return returnString