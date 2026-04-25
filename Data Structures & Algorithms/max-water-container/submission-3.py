class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = -1
        start = 0

        while start < len(heights):
            end = start + 1
            while end < len(heights):
                tmp_height = min(heights[start],heights[end])
                tmp_gap = end - start
                max_area = max(max_area, tmp_height * tmp_gap)
                end += 1
            start += 1
        
        return max_area