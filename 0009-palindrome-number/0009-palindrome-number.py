class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums=str(x)[::-1]
        if x <0:
            return False
        if str(x) == nums:
            return True
        else:
            return False