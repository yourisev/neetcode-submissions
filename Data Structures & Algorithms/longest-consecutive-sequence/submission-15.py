import math

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = {}
        for num in nums:
            seen[num] = False
        
        longest_seq_len = -math.inf
        for num in nums:
            curr_length = 1
            seen[num] = True
            next_num = num + 1

            while next_num in seen.keys() and seen[next_num] == False:
                curr_length += 1
                seen[next_num] = True
                next_num += 1
            
            prev_num = num - 1
            while prev_num in seen.keys() and seen[prev_num] == False:
                curr_length += 1
                seen[prev_num] = True
                prev_num -= 1
            
            longest_seq_len = max(longest_seq_len, curr_length)
        
        return max(0,longest_seq_len)