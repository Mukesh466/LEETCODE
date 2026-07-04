class Solution:
    def countSegments(self, s: str) -> int:
        cout=0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                cout += 1
        return cout
      #it checks for any space present or not if any space is there then it will omit and jumps to next element
