class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = list()

        for x in nums:
            if x in d:
                return True
            d.append(x)
        return False
        