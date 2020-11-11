#
# @lc app=leetcode id=854 lang=python3
#
# [854] K-Similar Strings
#

# @lc code=start
class Solution:
    '''
    思路：
        1. 此题最开始我想用DFS来实现，问题在于不一定能保证最短路径，超时
        2. 使用BFS+MEMO来实现，通过记录看到过的替换字符串，避免重复计算
        3. 在进行替换的时候只需要找到第一个不同的字符，同时找到后续所有满足j位置上不直接和Bj相等的元素生成替换字符串
        4. 见到B被生成出来，即刻返回答案
        5. BFS保证路径最短
        其难度在于寻找BFS过程中新的state的生成模式，需要思考
    '''
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0
        res = 0
        q = collections.deque([A])
        seen = set([A])
        while q:
            res += 1
            new_q = collections.deque()
            while q:
                s = q.popleft()
                i = 0
                while s[i] == B[i]: i+=1
                for j in range(i+1, len(B)):
                    if s[j] == B[j] or B[i] != s[j]:
                        continue
                    new_s = s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
                    if new_s not in seen:
                        seen.add(new_s)
                        new_q.append(new_s)
                        if new_s == B:
                            return res
            q = new_q
        return res

# @lc code=end

