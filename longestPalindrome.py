class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for ch in s:
            if ch in counts:
                counts[ch]+= 1
            else:
                counts[ch]= 1

        total = 0
        found_odd = False
        for ch in counts:
            c = counts[ch]

            total += (c // 2) * 2 
            if c % 2 ==1:
                found_odd = True
        if found_odd:
            total+= 1
        return total
