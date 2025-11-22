class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        connections = defaultdict(list)
        for u, v in adjacentPairs:
            connections[u].append(v)
            connections[v].append(u)
        start_num = None
        for num in connections:
            if len(connections[num]) == 1:
                start_num = num
                break
        n = len(adjacentPairs) + 1
        result = [start_num]
        
        prev = None 
        curr = start_num
        for _ in range(n - 1):
            neighbors = connections[curr]
            next_num = None
            if neighbors[0] != prev:
                next_num = neighbors[0]
            else:
             
                if len(neighbors) > 1:
                    next_num = neighbors[1]

            if next_num is not None:
                result.append(next_num)
                prev = curr
                curr = next_num
        return result