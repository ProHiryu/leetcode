#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.dfs("", S, res)
        return res

    def dfs(self, pre, s, res):
        if s == '':
            res.append(pre)
            return
        if s[0].isdigit():
            self.dfs(pre + s[0], s[1:], res)
        else:
            self.dfs(pre + s[0].lower(), s[1:], res)
            self.dfs(pre + s[0].upper(), s[1:], res)
# @lc code=end

