class Solution:
    def isValid(self, s: str) -> bool:

        ans=[]
        
        for ch in s:
            if ch in "{([":
                ans.append(ch)
                
            else:
                if not ans:
                    return False
                top=ans.pop()
                if ch == ")" and top !="(":
                    return False
                if ch == "}" and top !="{":
                    return False
                if ch == "]" and top !="[":
                    return False
        return not ans