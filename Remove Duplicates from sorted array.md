# Remove Duplicates from Sorted Array

Given a sorted array of integers, remove the duplicate elements in-place such that each unique element appears only once.
Return the number of unique elements.

# Approach:

Since the array is already sorted, duplicate elements will be next to each other.
We use:
One pointer to track the position of unique elements.
Another pointer to traverse the array.

# Algorithm:
Start from the second element.
Compare the current element with the previous unique element.
If different, move it to the next unique position.
Continue until the end of the array.
Return the count of unique elements.
# Python code
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
# Time Complexity:
O(n)
<img width="527" height="319" alt="image" src="https://github.com/user-attachments/assets/1aec14d5-b0eb-4003-a8c1-197e8459bfc3" />

# Space complexity:
O(1)
<img width="515" height="331" alt="image" src="https://github.com/user-attachments/assets/be19b824-0d69-4617-9af1-a59c8e800669" />
