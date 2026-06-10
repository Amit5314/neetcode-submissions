class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        p = [1]*n
        s = [1]*n
        r = []
        for i in range(1,len(nums)):
            p[i] = p[i-1]*nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            s[i] = s[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            r.append(p[i]*s[i])
        
        return r
