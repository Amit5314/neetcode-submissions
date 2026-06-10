from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        m = float('-inf')

        d = defaultdict(int)

        for x in nums:
            d[x]+=1
        
        for x in nums:
            if x-1 not in d.keys():
                c = 1
                while x+1 in d.keys():
                    c = c + 1
                    x = x + 1
                m = max(c,m)
        
        return 0 if m == float('-inf') else m