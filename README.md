# Remove Duplicates from Sorted Array
<img width="527" height="319" alt="image" src="https://github.com/user-attachments/assets/1aec14d5-b0eb-4003-a8c1-197e8459bfc3" />
<img width="515" height="331" alt="image" src="https://github.com/user-attachments/assets/be19b824-0d69-4617-9af1-a59c8e800669" />
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        for j in range(1,len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i +=1
        return i

```
