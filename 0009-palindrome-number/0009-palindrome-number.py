class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)[::-1]
        if x < 0:
            return False
        if str(x) == n:
            return True
        else:
            return False