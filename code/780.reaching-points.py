#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#

# @lc code=start
class Solution:
    '''
    从后往前看只会存在一条路径通往初始节点，如果一个个相减（大的减小的）则会超时
    using ty%=tx instead of while (tx > ty) { tx -= ty }即可
    '''
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
               sy == ty and sx <= tx and (tx - sx) % sy == 0
# @lc code=end

