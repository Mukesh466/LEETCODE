class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowel={'a','e','i','o','u','A','O','I','E','U'}
        left,right=0,len(s)-1
        while left < right:
            if s[left] not in vowel:
                left +=1
            elif s[right] not in vowel:
                right -=1
            else:
                s[left],s[right]=s[right],s[left]
                left +=1
                right -=1
        return ''.join(s)
#by using two pointers method 
