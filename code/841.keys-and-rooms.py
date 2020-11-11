#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set([0])
        N = len(rooms)
        state = [0]
        while state:
            r = state.pop()
            for i in rooms[r]:
                if i not in seen:
                    state.append(i)
                    seen.add(i)
            if len(seen) == N: return True
        return False
# @lc code=end

