class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = 1 if (i == 0) else result[i-1] * nums[i-1]
        
        for i in range(len(nums)-1,-1,-1):
            prod = 1 if (i == len(nums) - 1) else nums[i+1] * prod
            result[i] = result[i] * prod
        
        return result

        