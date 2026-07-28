class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked=set()
        for i in nums:
            if i in checked:
                return True
            checked.add(i)
        return False
        