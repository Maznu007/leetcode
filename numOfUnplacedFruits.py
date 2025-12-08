class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        baskets.sort() 
        j = 0
        unplaced = 0
        n = len(baskets)
        for f in fruits:
            while j < n and baskets[j] < f:
                j += 1

            if j < n:
                j += 1
            else:
                unplaced += 1
        return unplaced
