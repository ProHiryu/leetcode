#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # The times a number n occurs in the minimums is |left_bounday-indexof(n)| * |right_bounday-indexof(n)| 
        # The total sum is sum([n * |left_bounday - indexof(n)| * |right_bounday - indexof(n)| for n in array]
        res = 0
        stack = []  #  non-decreasing 
        A = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(A):
            # stack[-1], i is the left and right bounday
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1]) 
            stack.append(i)
        return res % (10**9 + 7)
# @lc code=end

