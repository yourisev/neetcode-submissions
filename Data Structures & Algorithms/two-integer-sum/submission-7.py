class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        size_nums = len(nums)
        seen = {}
        for i in range(size_nums):
            rest = target - nums[i]
            if seen.get(rest,-1) == -1:
                seen[nums[i]] = i
            else:
                return [seen[rest],i]
        
        return []