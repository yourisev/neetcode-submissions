import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num]+= 1
        
        heap = []
        for f_k, v in frequencies.items():
            f = v
            s = f_k
            heapq.heappush(heap,(f,s))
            if  len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for f, s in heap:
            result.append(s)
        return result
        