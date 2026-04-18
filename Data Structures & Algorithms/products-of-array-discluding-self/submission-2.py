class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        nums_size = len(nums)
        result = [1] * nums_size
        for i in range(nums_size):
            j = 0
            while j < nums_size:
                if j == i:
                    j += 1
                    continue
                result[i] *= nums[j]
                if nums[j] == 0:
                    break
                j += 1
        
        return result


        