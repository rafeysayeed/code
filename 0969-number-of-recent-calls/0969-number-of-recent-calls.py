class RecentCounter(object):

    def __init__(self):
        self.requests = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        [1,100,3001]
        """ 
        # # Time Limit Exceeds
        # self.requests.append(t)
        # n = 0
        # for i in range(len(self.requests)-1, -1, -1):
        #     if self.requests[i] + 3000 < t:
        #         continue
        #     else:
        #         n += 1
        # return n

        if len(self.requests) == 0:
            self.requests.append(t)
            return 1
        else:
            margin = t - 3000
            while len(self.requests) != 0 and self.requests[0] < margin:
                self.requests.pop(0)
            self.requests.append(t)
            return len(self.requests)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)