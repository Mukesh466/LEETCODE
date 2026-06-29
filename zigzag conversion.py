class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i = 0
        d = 0
        rows = [[] for _ in range(numRows)]
        for ch in s:
            rows[i].append(ch)
            if i == 0:
                d = 1
            elif i == numRows-1:
                d = -1
            i += d

        res = ''
        for i in range(numRows):
            res += ''.join(rows[i])
        return res

        #storing diagonal zigzag pattern (d = 1 means moving downwards , d = 0 means moving upwards)
