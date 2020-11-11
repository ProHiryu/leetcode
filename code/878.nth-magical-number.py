#
# @lc app=leetcode id=878 lang=python3
#
# [878] Nth Magical Number
#

# @lc code=start
class Solution:
    '''
    Suppose A =2 and B = 3, then the lcm is 6. The list of magical number less or equal to 6 is [2,3,4,6]. 
    Then, the 1st to 4th magical number to [2,3,4,6], the 5th to 8th number is 6 added to [2,3,4,6] respectively, the 9th to 12nd number is 6*2 added to [2,3,4,6] respectively, and so on.

    So, the key here is to get all the magical number less or equal to the lcm of A and B. Then, the Nth number can be obtained immediately.
    '''
    def gcd(self, x, y):
        while y > 0:
            x, y = y, x % y
        return x

    def lcm(self, x, y):
        return x*y//self.gcd(x,y)

    def nthMagicalNumber(self, N, A, B):
        temp = self.lcm(A,B)
        seq = {}
        for i in range(1,temp//A+1):
            seq[i*A] = 1
        for i in range(1,temp//B+1):
            seq[i*B] = 1
        cand = sorted([key for key, value in seq.items()])
        ans = ((N-1)//len(cand))*cand[-1] + cand[N%len(cand)-1]
        return ans % (10**9+7)
# @lc code=end

