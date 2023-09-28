class RandomizedCollection(object):

    def __init__(self):
        self.listed = []

    def insert(self, val):
        if val not in self.listed:
            self.listed.append(val)
            return True
        else:
            self.listed.append(val)
            return False

    def remove(self, val):
        if val in self.listed:
            self.listed.remove(val)
            return True
        else:
            return False
        
    def getRandom(self):
        if len(self.listed):
            return random.choice(self.listed)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()