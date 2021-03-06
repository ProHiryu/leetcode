#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsperbucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.itemsperbucket

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket_num = self.hash(key)
        if not self.table[bucket_num]:
            self.table[bucket_num] = [-1 for _ in range(self.itemsperbucket)]
        bucket_pos = self.pos(key)
        self.table[bucket_num][bucket_pos] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket_num = self.hash(key)
        if not self.table[bucket_num]:
            return -1
        bucket_pos = self.pos(key)
        return self.table[bucket_num][bucket_pos]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket_num = self.hash(key)
        bucket_pos = self.pos(key)
        if self.table[bucket_num]:
            self.table[bucket_num][bucket_pos] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

