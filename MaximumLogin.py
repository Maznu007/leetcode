class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        countL = 0
        CountLC = 0
        base = 0
        for i in s: #Count base number of "LCT"
            if i == 'L':
                countL += 1
            elif i == 'C':
                CountLC += countL
            elif i == 'T':
                base += CountLC
        prefixL = [0] * (n+1)
        prefixLC = [0] * (n+1)
        countL = 0
        lc = 0
        prefixL[0] = 0
        prefixLC[0] = 0
        for i in range(n): #Prefix counts
            ch = s[i]
            if ch == 'L':
                countL += 1
            elif ch == 'C':
                lc += countL
            prefixL[i+1] = countL
            prefixLC[i+1] = lc
        suffixT = [0] * (n+1)
        suffixCT = [0] * (n+1)
        countT = 0
        ct = 0
        suffixT[n] = 0
        suffixCT[n] = 0
        for i in range(n-1, -1, -1): #Suffix counts
            ch = s[i]
            if ch == 'T':
                countT += 1
            elif ch == 'C':
                ct += countT
            suffixT[i] = countT
            suffixCT[i] = ct
        bestL = 0
        bestC = 0
        bestT = 0
        for i in range(n): #Calculate best gains
            bestL = max(bestL,suffixCT[i])
            bestT = max(bestT,prefixLC[i])
            bestC = max(bestC,prefixL[i]*suffixT[i])
        bestGain = max(bestL,bestC,bestT,0)
        return base + bestGain