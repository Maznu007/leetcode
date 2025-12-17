class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        answer = 0
        descent_length = 0
        for i in range(n):
            if i>0 and prices[i] == prices[i-1]-1:
                descent_length += 1
            else:
                descent_length = 1
            answer += descent_length
        return answer 