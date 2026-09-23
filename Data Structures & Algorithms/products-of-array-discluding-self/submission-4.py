class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        nums_sz = len(nums)

        res = [1 for _ in range(nums_sz)]

        for i in range(nums_sz):
            res[i] = res[i-1] * nums[i-1] if i > 0 else res[i]
        
        tmp = 1
        for i in range(nums_sz - 1, -1, -1):
            res[i] = res[i] * tmp
            tmp *= nums[i]
        
        return res
