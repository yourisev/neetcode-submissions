# O(n) Time Complexity and O(n) Space Complexity

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True
        #     seen.add(nums[i])
        for num in nums :
            if num in seen:
                return True
            seen.add(num)
        
        return False

        
        