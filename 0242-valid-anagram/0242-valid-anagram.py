class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            occurance1=collections.Counter(s)
            occurance2=collections.Counter(t)
            if occurance1 == occurance2:
                return True
            else:
                return False
        return False
