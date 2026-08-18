class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        count=0
        for i in nums_set:
            if i-1 not in nums_set:
                curr=i
                length=1
                while curr+1 in nums_set:
                    length +=1
                    curr +=1
                count=max(count,length)
        return count