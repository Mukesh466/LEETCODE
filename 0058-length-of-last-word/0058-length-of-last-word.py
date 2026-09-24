class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lent=0
        
        i=len(s)-1
        while i>=0 and s[i] == ' ' :
            i-=1
        while i>=0 and s[i] != ' ':
            lent +=1
            i-=1
        return lent