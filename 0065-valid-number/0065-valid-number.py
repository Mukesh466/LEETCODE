class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            return (float(s) or float(s)==0) and not ("n" in s)
        except:
            return False