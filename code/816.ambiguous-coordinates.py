#
# @lc app=leetcode id=816 lang=python3
#
# [816] Ambiguous Coordinates
#

# @lc code=start
class Solution:
    '''
    思路：
        if S == "": return []
        if S == "0": return [S]
        if S == "0XXX0": return []
        if S == "0XXX": return ["0.XXX"]
        if S == "XXX0": return [S]
        return [S, "X.XXX", "XX.XX", "XXX.X"...]
    '''
    def ambiguousCoordinates(self, S: str) -> List[str]:
        S = S[1:-1]
        def f(S):
            if not S or len(S) > 1 and S[0] == S[-1] == '0': return []
            if S[-1] == '0': return [S]
            if S[0] == '0': return [S[0] + '.' + S[1:]]
            return [S] + [S[:i] + '.' + S[i:] for i in range(1, len(S))]
        return ['(%s, %s)' % (a, b) for i in range(len(S)) for a, b in itertools.product(f(S[:i]), f(S[i:]))]
# @lc code=end

