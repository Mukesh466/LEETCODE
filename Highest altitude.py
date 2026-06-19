class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        calt=0
        malt=0
        for i in gain:
            calt += i 
            malt = max(malt,calt)
        return malt
        
