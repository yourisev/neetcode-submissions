class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = -1
        start = 0
        end = len(heights) - 1

        while start < end:
            tmp_height = min(heights[start],heights[end])
            tmp_gap = end - start
            max_area = max(max_area, tmp_height * tmp_gap)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return max_area