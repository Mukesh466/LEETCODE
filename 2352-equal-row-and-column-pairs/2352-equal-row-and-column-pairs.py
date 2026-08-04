from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        pairs=0
        row=defaultdict(int)
        for i in grid:
            row[tuple(i)] +=1
        for cols in range(n):
                column=tuple(grid[j][cols] for j in range(n))
                if column in row:
                    pairs += row[column]
        return pairs