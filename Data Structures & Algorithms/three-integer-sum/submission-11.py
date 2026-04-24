class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result_set = set()
        result = []

        sorted_nums = sorted(nums)
        i = 0
        nums_len = len(nums)

        while i < nums_len - 2:
            j = i + 1
            k = nums_len - 1
            
            while j < k:
                tmp = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                
                if tmp == 0:
                    result_set.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    tmp_j = j
                    tmp_k = k
                    while j < k and sorted_nums[j] == sorted_nums[j + 1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[ k - 1]:
                        k -= 1
                    if j == tmp_j:
                        j += 1
                    if k == tmp_k: 
                        k -= 1
                elif tmp < 0:
                    tmp_j = j
                    while j + 1 < k and sorted_nums[j] == sorted_nums[j + 1]:
                        j += 1
                    if j == tmp_j:
                        j += 1
                else:
                    tmp_k = k
                    while j < k - 1 and sorted_nums[k] == sorted_nums[ k - 1]:
                        k -= 1
                    if k == tmp_k: 
                        k -= 1
            i += 1

        
        for val in result_set:
            result.append([val[0],val[1],val[2]])


        return result