#
# @lc app=leetcode id=715 lang=python3
#
# [715] Range Module
#

# @lc code=start
class RangeModule:

    def __init__(self):
        # range内包含所有interval的起点终点，其中每次新进来一个interval，先查询首尾位置
        # 如果li，ri任意一个mod2为0，说明他们都在当前范围内
        #   如果此时是增加，则取对应的interval，重新赋值一下即可（取上一个和下一个，将当前范围全部覆盖掉即可）
        #   如果此时是删除，则不需要做处理
        # 如果li，ri任意一个mod2为1，则说明他们不在对应的范围内
        #   如果此时是增加，则不需要做处理，将对应的范围覆盖一下即可
        #   如果此时是删除，则需要取前一个和后一个（将中间的全部删除）
        self.range = [-float('inf'), float('inf')]

    def addRange(self, left, right):
        self._updateRange(left, right, 0)
        
    def queryRange(self, left, right):
        # 查找对应的interval范围
        li = bisect.bisect(self.range, left)
        ri = bisect.bisect_left(self.range, right)
        return li == ri and li % 2 == 0
    
    def removeRange(self, left, right):
        self._updateRange(left, right, 1)

    def _updateRange(self, left, right, op):
        li = bisect.bisect_left(self.range, left)
        ri = bisect.bisect(self.range, right)
        
        if li % 2 == op:
            li = li - 1
            left = self.range[li]
        if ri % 2 == op:
            right = self.range[ri]
            ri += 1
            
        self.range[li:ri] = [left, right]

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# @lc code=end

