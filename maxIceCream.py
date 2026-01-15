class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if coins <= 0 or not costs:
            return 0
        max_price = max(costs)
        jars = [0] * (max_price + 1)
        for price in costs:
            jars[price]+= 1
        total_ice_creams = 0
        for price in range(1, max_price + 1):
            if jars[price]==0:
                continue
            if price >coins:
                break
            a = coins // price
            buy =min(jars[price], a)
            total_ice_creams += buy
            coins-= buy *price
        return total_ice_creams