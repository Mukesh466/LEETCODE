class Solution:
    def isValid(self, s: str) -> bool:

        res=[]
        
        for ch in s:
            if ch in "{([":
                res.append(ch)
            else:
                if not res:
                    return False
                top=res.pop()
                if ch == ")" and top !="(":
                    return False
                if ch == "}" and top !="{":
                    return False
                if ch == "]" and top !="[":
                    return False
        return not res