class Solution:
    def fib(self, n: int) -> int:
        sq = 5 ** 0.5
        fib = ((1 + sq) / 2) ** n- ((1-sq) / 2) ** n
        return round(fib / sq)


#or
class solution:
  def fib(self,n: int) -> int:
    if n <= 1:
      return n
    return self.fib(n-1) + self.fib(n-2)
