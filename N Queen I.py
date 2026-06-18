class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[["."] * n for _ in range(n)]
        cols=set()
        dia1=set()
        dia2=set()
        def backtrack(rows):
            if rows == n:
                res.append(["".join(r) for r in board])
                return 
            for col in range(n):
                if col in cols:
                    continue
                if (rows-col) in dia1:
                    continue
                if (rows+col) in dia2:
                    continue

                board[rows][col] = "Q"
                cols.add(col)
                dia1.add(rows-col)
                dia2.add(rows+col)
                backtrack(rows+1)

                board[rows][col] = "."

                cols.remove(col)
                dia1.remove(rows-col)
                dia2.remove(rows+col)  
        backtrack(0)
        return res              
