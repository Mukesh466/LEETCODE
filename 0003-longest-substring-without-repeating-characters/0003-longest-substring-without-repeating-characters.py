class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxi=0
        common=set()
        for right in range(len(s)):
            while s[right] in common:
                common.remove(s[left])
                left+=1
            common.add(s[right])
            maxi=max(maxi,len(common))
        return maxi
