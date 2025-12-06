from typing import List
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        prices = [INF] * n
        prices[src] = 0
        
        for i in range(k + 1):
            temp_prices = list(prices)
            for frm, to, price in flights:
                if prices[frm] == INF:
                    continue
                
                new_price = prices[frm] + price
                temp_prices[to] = min(temp_prices[to], new_price)
            prices = temp_prices
            
        result = prices[dst]
        
        if result != INF:
            return int(result)
        else:
            return -1