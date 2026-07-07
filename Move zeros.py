class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left =0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[left]=nums[left],nums[i]
                left +=1
        return nums
      #in this we check for the non 0 values and then it swaps to right and move the right value to left 
        
