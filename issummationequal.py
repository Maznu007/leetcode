class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def getnumerical(word):
            numerical = 0
            for char in word:
                letterval= ord(char) - ord("a")
                numerical = numerical* 10 +letterval
            return numerical
        val1 = getnumerical(firstWord)
        val2 =getnumerical(secondWord)
        val3 = getnumerical(targetWord)
        return val1 + val2 == val3