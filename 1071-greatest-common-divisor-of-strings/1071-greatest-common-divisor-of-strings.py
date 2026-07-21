class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        for i in range(len(str2), 0, -1):
            gcd = str2[:i]
            if(
                gcd * (len(str1) // i) == str1 
                and gcd * (len(str2) // i) == str2
            ): return gcd
        return ""