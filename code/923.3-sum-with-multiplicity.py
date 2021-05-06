#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

# @lc code=start
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        cnt, ans = collections.Counter(arr), 0
        for i in cnt:
            for j in cnt:
                k = target - i - j
                if i == j == k:
                    ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
                elif i == j:
                    ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[k]
                elif i < j < k:
                    ans += cnt[i] * cnt[j] * cnt[k]
        return ans % (10**9 + 7)
# @lc code=end

