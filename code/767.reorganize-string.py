#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    '''
    1. 构建一个最大堆，按照出现频率进行排序，使用heap负数实现，带上字母
    2. 每次拿出频率最高的字母，放到当前答案位置上，同时将次数-1（程序+1），保存在p_a中
    3. 如果还是没有使用完当前字母则入堆
    4. 由于之前已经对可行性做过判断，没有任何字母是会超过当前数字一半以上的，所以可以保证不会有同样字母拿到
    '''
    def reorganizeString(self, S: str) -> str:
        res, c = [], Counter(S)
        for key, value in c.items():
            if value > ( len(S) + 1 ) // 2: return ''
        pq = [(-value,key) for key,value in c.items()]
        heapq.heapify(pq)
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        res = ''.join(res)
        return res
        
# @lc code=end

