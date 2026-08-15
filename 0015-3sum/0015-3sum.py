class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i !=0:
                continue
            l=i+1
            r=len(nums)-1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if tot > 0:
                    r-=1
                elif tot < 0 :
                    l +=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] ==nums[l-1]:

                        l+=1
        return res