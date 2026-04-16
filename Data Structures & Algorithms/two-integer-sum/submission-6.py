class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        size_nums = len(nums)
        for i in range(size_nums):
            for j in range(i+1,size_nums):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        return []