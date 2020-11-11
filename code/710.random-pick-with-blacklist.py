#
# @lc app=leetcode id=710 lang=python3
#
# [710] Random Pick with Blacklist
#

# @lc code=start
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        b = set(blacklist)
        self.valid_num = N - len(b) # actual valid numbers is N - |B|
        self.remap = {} # we need to map numbers to [N - |B|, N] which in blacklist & less than N - |B|
        need_map = []
        for x in b:
            if x < self.valid_num:
                need_map.append(x) # numbers need to be mapped
        j = 0
        for i in range(self.valid_num, N):
            if i not in b: # numbers can be returned
                self.remap[need_map[j]] = i
                j += 1

    def pick(self) -> int:
        idx = random.randint(0, self.valid_num - 1)
        return self.remap[idx] if idx in self.remap else idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
# @lc code=end

