from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for x in strs:
            sorts = "".join(sorted(x))
            d[sorts].append(x)
        
        res = list()
        for e in d.values():
            res.append(e)
        
        return res
            