class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        def backtrack(start, target):
            if target == 0:
                result.append(path.copy())
                return
            if target< 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i -1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i])

                path.pop()

        backtrack(0, target)
        return result
