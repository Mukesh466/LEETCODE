class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=set(nums)
        mini=min(nums)
        maxi=max(nums)
        li=[]
        for i in range(mini,maxi+1):
            if i not in s:
                li.append(i)
        return li
        