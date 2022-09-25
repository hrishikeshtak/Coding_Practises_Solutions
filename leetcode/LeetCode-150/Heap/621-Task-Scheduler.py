"""
621. Task Scheduler
"""

from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Each task is done in 1 unit of time
        # we will add count of each char into maxHeap
        
        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)
        q = deque()  # [-cnt, Time]
        time = 0
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                # add 1 bcoz -ve number in heap and need to decrease counter
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
                
            if q:
                if time == q[0][1]:
                    heapq.heappush(maxHeap, q.popleft()[0])
        return time
