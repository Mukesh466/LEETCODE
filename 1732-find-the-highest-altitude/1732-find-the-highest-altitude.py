class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curralt=0
        maxalt=0
        for i in gain:
            curralt += i 
            maxalt = max(maxalt,curralt)
        return maxalt