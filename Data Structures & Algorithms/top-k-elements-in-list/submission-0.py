from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        heap = [(-v,k) for k,v in freq.items()]

        heapq.heapify(heap)

        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k = k - 1
        
        return res