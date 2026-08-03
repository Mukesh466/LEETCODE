from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=defaultdict(int)
        for i in arr:
            count[i] +=1
        occured=list(count.values())
        return len(occured) == len(set(occured))
        