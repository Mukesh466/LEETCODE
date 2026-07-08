class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i +=1
            j +=1
        return i == len(s)
      #s and t are the string where t is the main string and s is substring
      #we comparing with both the element if it is presented in the substring then increment or else move to next element in the main string 
