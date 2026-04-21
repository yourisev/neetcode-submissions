import math

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set()
        for num in nums:
            seen.add(num)
        
        longest_seq_len = -math.inf
        for num in nums:
            curr_length = 1
            if num - 1 not in seen:
                next_num = num + 1
                while next_num in seen:
                    curr_length += 1
                    next_num += 1
                longest_seq_len = max(longest_seq_len, curr_length)
        
        return max(0,longest_seq_len)