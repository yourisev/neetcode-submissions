class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 1 if len(nums) != 0 else 0
        for i in range(len(nums)):
            start = nums[i]
            count = 1
            while True:
                j = 0
                while j < len(nums) and nums[j] != start + count:
                    j += 1
                
                if j != len(nums):
                    count += 1
                else:
                    break

            longest = max(longest, count)
        return longest