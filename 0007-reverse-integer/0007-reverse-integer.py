class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign =-1
        else:
            sign =1
        x=abs(x)
        rem=0
        while x > 0:
            ld=x%10
            rem=(rem*10)+ld
            x=x//10
        rem *=sign
        if rem < -2**31 or rem > 2 **31 - 1:
            return 0
        return rem
