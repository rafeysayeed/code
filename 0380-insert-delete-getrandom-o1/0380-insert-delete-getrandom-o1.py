class RandomizedSet(object):

    def __init__(self):
        self.listed = []

    def insert(self, val):
        if val not in self.listed:
            self.listed.append(val)
            return True
        else:
            return False

    def remove(self, val):
        if val in self.listed:
            self.listed.remove(val)
            return True
        else:
            return False
        
    def getRandom(self):
        return random.choice(self.listed)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()