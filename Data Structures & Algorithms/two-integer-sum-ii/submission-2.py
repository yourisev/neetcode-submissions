class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left <= right :

            while numbers[left] + numbers[right] > target:
                right -= 1
            
            while numbers[right] + numbers[left] < target:
                left += 1
            
            if numbers[right] + numbers[left] == target:
                return [left+1, right+1]
        
        return []
            