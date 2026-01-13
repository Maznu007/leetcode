class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = []
        B = []
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    A.append((r, c))
                if img2[r][c] == 1:
                    B.append((r, c))
        shift_count = {}
        best = 0
        for (r1, c1) in A:
            for (r2, c2) in B:
                shift = (r2 - r1, c2 - c1)
                if shift not in shift_count:
                    shift_count[shift] = 0
                shift_count[shift] += 1
                best = max(best, shift_count[shift])
        return best