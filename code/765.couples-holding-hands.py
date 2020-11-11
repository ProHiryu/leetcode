#
# @lc app=leetcode id=765 lang=python3
#
# [765] Couples Holding Hands
#

# @lc code=start
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d, swap={}, 0
        for i, x in enumerate(row):
            d[x]=i
        for i in range(0, len(row), 2):
            partner=row[i]+1 if row[i]%2==0 else row[i]-1
            j=d[partner]
            if j-i!=1:
                row[i+1], row[j]=row[j], row[i+1]
                d[row[j]]=j
                swap+=1
        return swap
# @lc code=end

