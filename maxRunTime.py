class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        
        low = 0
        high =total//n
        
        def can_run(Temp):
            available = 0
            for i in batteries:
                available += min(i,Temp)
                if available >= Temp * n:
                    return True
            return available >= Temp * n

        while low < high:
            mid =low + (high- low+ 1) //2
            if can_run(mid):
                low =mid
            else:
                high = mid - 1
        return low
