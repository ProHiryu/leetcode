#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#

# @lc code=start
class Solution:
    '''
    思路：
        1. L只能向左边移动
        2. R只能向右边移动
        3. 对于Start当中所有的L都不能比end当中的靠后，同时顺序要一样
        4. 对于Start当中所有的R都不能比end当中的靠前，同时顺序要一样
    '''
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end): return False
        
        A = [(s, idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
        B = [(e, idx) for idx, e in enumerate(end) if e == 'L' or e == 'R']
        if len(A) != len(B): return False
        
        for (s, i), (e, j) in zip(A, B):
            if s != e: return False
            if s == 'L':
                if i < j:
                    return False
            if s == 'R':
                if i > j:
                    return False
            
        return True
# @lc code=end

