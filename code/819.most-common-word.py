#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
        
# @lc code=end

