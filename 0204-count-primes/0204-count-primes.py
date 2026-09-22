class Solution:
    def countPrimes(self, n: int) -> int:

        seen=[0]*n
        count=0

        for i in range(2,n):
            if seen[i]:
                continue
            count +=1
            seen[i*i:n:i] = [1] * ((n-1) // i-i+1)

        return count