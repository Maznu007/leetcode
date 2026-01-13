class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n=len(heights)
        max_total_sum= 0
        for i in range(n):
            current_sum =heights[i]
            last_height = heights[i]
            for j in range(i- 1,-1, -1):
                last_height =min(heights[j],last_height)
                current_sum += last_height
                
            last_height= heights[i]
            for j in range(i + 1,n):
                last_height = min(heights[j],last_height)
                current_sum += last_height          
            max_total_sum =max(max_total_sum,current_sum)
        return max_total_sum