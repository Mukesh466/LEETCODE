class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign =-1
        else:
            sign =1
        x=str(abs(x))[::-1]
        result=sign*int(x)
        if result < -2 **31 or result > 2**31 -1:
            return 0
        return result