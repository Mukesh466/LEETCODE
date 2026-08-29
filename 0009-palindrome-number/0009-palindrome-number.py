class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)[::-1]
        if x < 0:
            return False
        if str(x) == num:
            return True
        else:
            return False