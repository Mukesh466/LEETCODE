class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            left,right = (i==0) or (flowerbed[i-1] == 0),(i==(len(flowerbed)-1)) or (flowerbed[i+1]==0)
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n-=1
                if n==0:
                    return True
        return False
      #greedy algorithm it is uses the current best choice and move fowards unlike  dynamic programming this algorithm will not go back
