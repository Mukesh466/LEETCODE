class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq={}
        for ch in s1:
            freq[ch]=freq.get(ch,0)+1


        window={}
        for i in range(len(s1)):
            ch=s2[i]
            window[ch]=window.get(ch,0)+1


        left=0
        right=len(s1)-1

    
        if freq == window:
                return True

            
        while right+1 < len(s2):
            window[s2[left]] -=1
            if window[s2[left]] ==0:
                del window[s2[left]]

            window[s2[right+1]] =window.get(s2[right+1],0)+1

            left +=1
            right +=1

            if freq == window:
                return True
                
        return False