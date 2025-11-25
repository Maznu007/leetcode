class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        n = len(nums)
        mindif = math.inf 
        for i in range(n-k+1):
            curr = nums[n-k+1]-nums[i]
            mindif = min(mindif,curr)
        return int(mindif)