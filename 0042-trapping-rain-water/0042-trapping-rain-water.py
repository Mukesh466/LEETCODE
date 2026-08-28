class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftmaxi=height[left]
        rightmaxi=height[right]
        water=0
        while left < right:
            if height[left] < height[right]:
                left +=1
                leftmaxi=max(leftmaxi,height[left])
                water +=leftmaxi-height[left]
            else:
                right-=1
                rightmaxi=max(rightmaxi,height[right])
                water +=rightmaxi-height[right]
        return water