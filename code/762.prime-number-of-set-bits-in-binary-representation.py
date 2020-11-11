#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(map(lambda x: bin(x).count('1') in primes, range(L, R+1)))
# @lc code=end

