from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_d = defaultdict(int)
        for n in nums:
            num_d[n] += 1
        
        heap = []
        for item in num_d.items():
            heapq.heappush(heap,(-1*item[1], item[0]))
        
        num_l = []
        for _ in range(k):
            n = heapq.heappop(heap)
            num_l.append(n[1])
        return num_l
