class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_dist = 0
        last_person_index = -1
        for i in range(n):
            if seats[i] ==1:
                if last_person_index == -1:
                    current_dist= i  
                else:
                    gap_length = i - last_person_index
                    current_dist = gap_length // 2
                max_dist =max(max_dist,current_dist)
                last_person_index = i
        trailing_dist = n-1 -last_person_index
        max_dist = max(max_dist,trailing_dist)
    
        return max_dist
