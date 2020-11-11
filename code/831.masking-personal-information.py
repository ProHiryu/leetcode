#
# @lc app=leetcode id=831 lang=python3
#
# [831] Masking Personal Information
#

# @lc code=start
class Solution:
    def maskPII(self, S: str) -> str:
        at = S.find('@')
        if at >= 0:
            return (S[0] + "*" * 5 + S[at - 1:]).lower()
        S = "".join(i for i in S if i.isdigit())
        return ["", "+*-", "+**-", "+***-"][len(S) - 10] + "***-***-" + S[-4:]
# @lc code=end

