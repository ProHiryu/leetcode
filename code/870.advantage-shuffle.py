#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
class Solution:
    '''
    思路：
        1. 先将A B都排序
        2. 从大到小对B进行遍历，如果A的最大值大于b，则将其按顺序放到对应的dict中
        3. 在最后得到答案的时候如果dict当中有值则放到对应的位置，如果没有则直接从A当中取
    '''
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A)
        take = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b < A[-1]: take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]
# @lc code=end

