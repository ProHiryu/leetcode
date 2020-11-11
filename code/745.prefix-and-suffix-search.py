#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#

# @lc code=start
class WordFilter:

    def __init__(self, words: List[str]):
        self.weights = {}
        for weight, word in enumerate(words):
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    self.weights[word[:i] + '#' + word[j:]] = weight

    def f(self, prefix: str, suffix: str) -> int:
        return self.weights.get(prefix + '#' + suffix, -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end

