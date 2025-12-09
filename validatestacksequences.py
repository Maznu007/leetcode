class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk =[]
        popindex = 0
        for i in pushed:
            stk.append(i)
            while stk and popindex < len(popped) and stk[-1] == popped[popindex]:
                stk.pop()
                popindex+=1
        if not stk:
            return True
        else:
            return False