class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check=set()
        for i in nums:
            if i in check:
                return True
            check.add(i)
        return False
        