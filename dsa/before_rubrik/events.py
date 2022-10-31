from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        taken_days=set([])
        count=0
        events.sort(key=lambda e: e[1]-e[0])
        print(events)
        for e in events:
            for i in range(e[0],e[1]+1):
                if i not in taken_days:
                    count+=1
                    taken_days.add(i)
                    print("day", i, e)
                    break
        return count
print(Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]]))