class Solution:
    def clearDigits(self, s: str) -> str:
        main = []
        for i in s:
            if i.isdigit():
                if main and not main[-1].isdigit():
                    main.pop()
                else:
                    main.append(i)
            else:
                main.append(i)
                
        return "".join(main)