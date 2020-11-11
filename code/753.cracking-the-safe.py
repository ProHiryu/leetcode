#
# @lc app=leetcode id=753 lang=python3
#
# [753] Cracking the Safe
#

# @lc code=start
class Solution:
    '''
    1. 设定初始密码000..00
    2. 从剩下的数字当中按照固定顺序选取一个，加在原来最后（n-1）个数字后，如果不在haspset当中则将其加入，并终止当前循环
    3. 总共循环k**n次，在这个循环中每次都使用前缀加上数字的方式嵌套循环如果：
        1. 循环结束没有不存在hashset当中的密码，则不需要动，意味着所有情况都遍历过了
        2. 循环当中出现了不存在的密码，则加入hashset，同时以该密码作为前缀继续遍历
    '''
    def crackSafe(self, n: int, k: int) -> str:
        ans = "0" * (n - 1)
        visits = set()
        for x in range(k ** n):
            current = ans[-n+1:] if n > 1 else ''
            for y in range(k - 1, -1, -1):
                if current + str(y) not in visits:
                    visits.add(current + str(y))
                    ans += str(y)
                    break
        return ans
# @lc code=end

