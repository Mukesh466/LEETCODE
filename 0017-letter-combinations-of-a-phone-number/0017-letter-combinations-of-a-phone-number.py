class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad={ "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res=[]
        def backtracking(index,curr):
                if index == len(digits):
                    res.append(curr)
                    return
                for ch in keypad[digits[index]]:
                    curr +=ch
                    backtracking(index+1,curr)
                    curr = curr[:-1]
        backtracking(0,"")
        return res