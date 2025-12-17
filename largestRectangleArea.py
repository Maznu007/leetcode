class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        n = len(heights)
        for i in range(n+1):
            if i == n:
                curheight = 0
            else:
                curheight = heights[i]
            while stk and curheight < heights[stk[-1]]:
                top = stk.pop()
                height = heights[top]
                if not stk:
                    width = i
                else:  
                    width = i - stk[-1] - 1
                area = height * width
                max_area = max(max_area, area)
            stk.append(i)
        return max_area