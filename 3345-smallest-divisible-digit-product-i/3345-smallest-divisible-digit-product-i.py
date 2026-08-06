class Solution:
    def smallestNumber(self, num: int, t: int) -> int:
        def check(n:int) -> bool:
            mul =1
            while n > 0:
                mul *= n % 10
                n //= 10
                if mul == 0:
                    break
            return mul % t == 0
        while not check(num):
            num +=1
        return num