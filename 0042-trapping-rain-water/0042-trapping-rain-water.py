class Solution:
    def trap(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        contains=0
        while left < right:
            if leftmax < rightmax:
                left+=1
                leftmax=max(leftmax,height[left])
                contains+=leftmax-height[left]
            else:
                right-=1
                rightmax=max(rightmax,height[right])
                contains+=rightmax-height[right]
        return contains
