class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        word=s.split()
        reverse=word[::-1]
        return " ".join(reverse)
        
