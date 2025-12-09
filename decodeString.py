class Solution:
    def decodeString(self, s: str) -> str:
        numstk =[]
        strstk = []
        curstr = ""
        curnum = 0

        for i in s:
            if i.isdigit():
                curnum = curnum *10 +int(i)
            elif i =="[":
                strstk.append(curstr)
                numstk.append(curnum)
                curstr = ""
                curnum =0
            elif i =="]":
                repeatnum = numstk.pop()
                prevstr = strstk.pop()
                curstr = prevstr + (curstr * repeatnum)
            else:
                curstr+=i
        return curstr