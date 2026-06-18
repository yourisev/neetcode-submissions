import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        for num, frequency in frequencies.items():
            buckets[frequency].append(num)

        result = []
        for i in range(len(buckets) - 1,0,-1):
            len_bucket = len(buckets[i])
            if len_bucket > 0:
                for num in buckets[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
        
        return []

        # heap = []
        # for num, frequency in frequencies.items():
        #     heapq.heappush(heap,(frequency,num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # result = []
        # for i in range(len(heap)):
        #     result.append(heap[i][1])
        # return result