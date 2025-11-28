class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for ch in s.lower():
            if 'a' <= ch <= 'z':
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1
        a = []
        count = 0
        for key, value in freq.items():
            while value >0 and value in a:
                value -=1
                count += 1
            a.append(value)
        return count
