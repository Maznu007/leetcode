class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1)

        ans = 0
        j = 0
        for i in range(n):
            start = tiles[i][0]
            end = start + carpetLen - 1

            while j < n and tiles[j][1] <= end:
                j += 1
            full = pref[j] - pref[i]
            partial = 0
            if j < n and tiles[j][0] <= end:
                partial = end - tiles[j][0] + 1
            ans = max(ans, full + partial)
        return ans
