#
# @lc app=leetcode id=805 lang=python3
#
# [805] Split Array With Same Average
#

# @lc code=start
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        """
        the average value of A is avg, test all k items's summations, 
        when any k_items_sum == k * avg, return True, else False
        
        for the target k_items_sum and k, we have k_items_sum / k == tot_sum / alen, 
        and k_items_sum must be an integer, k <= len(A) // 2
        so :
            - k_items_sum == tot_sum * k / alen == tot_sum * k // alen
            - tot_sum * k % alen == 0
            - gcd(tot_sum, alen) > 1             # because  k <= len(A) // 2   and  tot_sum * k % alen == 0 
        """
        alen, tot_sum = len(A), sum(A)
        end_k = (alen >> 1) + 1  # only need to test k <= alen//2 items's summations.
        
        P = [1]     # k_items_summation_bitmap
        # P[0] = 1 = 0x1:  stand for  0 items's summation is 0( 0x1 = 2^0)
        
        # P[k] is a bitmap for all k items's summations.  
        # For example, if P[3] == 0x111000,  then all the 3 items's summations can be 3, 4, 5.        
        # P_i [k] = (P_{i-1} [k - 1] << i) | (P_{i-1} [k])   # A[i] in the k items or not in the k items 
        for i in A:                                         
            P[1:end_k ] = [((p << i) | q) for p, q in zip(P, P[1:end_k ] + [0])]
            
        for k in range(1, end_k ):    # check k items sub sequence's summations.   
            # for the target k and k_items_sum:
            #   - tot_sum * k % alen == 0 
            #   - k_items_sum == tot_sum * k // alen
            if tot_sum * k % alen == 0 and P[k] & (1 << (tot_sum * k // alen)):
                return True
        return False
# @lc code=end

