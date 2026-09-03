class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern) != len(words):
            return False
        seen={}
        for p,w in zip(pattern,words):
            p_key=("p",p)
            w_key=("w",w)
            if  p_key in seen and  seen[p_key] != w:
                return False
            if w_key in seen and seen[w_key] != p:
                return False
            seen[p_key] = w
            seen[w_key] = p
        return True 