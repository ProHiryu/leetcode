#
# @lc app=leetcode id=927 lang=python3
#
# [927] Three Equal Parts
#

# @lc code=start
class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        
        num_ones = sum(A)
        
        if num_ones == 0:
            return [0, 2]
        
        if num_ones % 3 != 0:
            return [-1, -1]
        
        c = 0
        s1 = s2 = s3 = -1
        for idx,x in enumerate(A):
			# Find the first 1 in each part
            if x == 1:
                c += 1
            
            if c == 1 and s1 < 0:
                s1 = idx
                
            if c == num_ones//3 + 1 and s2 < 0:
                s2 = idx
                
            if c == num_ones*2//3 + 1 and s3 < 0:
                s3 = idx
                break
                
        n = len(A[s3:]) # The length of each part when all the leading 0's are removed
        
        if A[s1:s1+n] == A[s2:s2+n] and A[s2:s2+n] == A[s3:]:
            return [s1+n-1, s2+n]
        else:
            return [-1, -1]
# @lc code=end

