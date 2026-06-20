class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 1 if len(nums) != 0 else 0
        nums.sort()
        i = 0

        while i < len(nums):
            count = 1
            j = i + 1
            while j < len(nums) and (nums[i] + count == nums[j] or nums[i] + count - 1 == nums[j]):
                if nums[i] + count == nums[j] :
                    count += 1
                j += 1
            longest = max(longest, count)
            i += 1

        return longest