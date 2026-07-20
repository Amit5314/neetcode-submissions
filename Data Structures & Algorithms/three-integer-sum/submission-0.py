class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i in range(len(nums)):

            l = i+1
            r = len(nums)-1

            a = nums[i]

            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue

            while l < r:
                s = a + nums[l] + nums[r]
                if s > 0:
                    r = r - 1
                elif s < 0:
                    l = l + 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l = l + 1
                    r = r - 1
                    while nums[l] == nums[l-1] and l < r:
                        l = l + 1
            
        return res