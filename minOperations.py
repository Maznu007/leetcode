class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        deletions = 0
        for x in nums:
            ok =True
            for y in numsDivide:
                if y %x != 0:
                    ok= False
                    break
            if ok:
                return deletions
            deletions += 1

        return -1
