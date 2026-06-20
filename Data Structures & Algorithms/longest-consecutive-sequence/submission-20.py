class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 1 if len(nums) != 0 else 0
        
        num_set =set()

        for num in nums:
            num_set.add(num)
        
        for num in nums:
            if num - 1 not in num_set:
                count = 1
                while num + count in num_set:
                    count += 1
                longest = max(longest, count)
        return longest