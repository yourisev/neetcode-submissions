import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        
        heap = []
        for num, frequency in frequencies.items():
            heapq.heappush(heap,(frequency,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(len(heap)):
            result.append(heap[i][1])
        return result