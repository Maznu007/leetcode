class Solution:
    def removezero(self, x: int) -> int:
        s = str(x)
        nozero = s.replace("0", "")
        if not nozero:
            return 0
        return int(nozero)
    def countDistinct(self, n: int) -> int:
        countintn = set()
        for i in range(1, n + 1):
            transformedint = self.removezero(i)
            countintn.add(transformedint)
        return len(countintn)