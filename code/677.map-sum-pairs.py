#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#

# @lc code=start
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, key, val): 
        self.d[key] = val

    def sum(self, prefix):
        return sum(self.d[i] for i in self.d if i.startswith(prefix))
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

