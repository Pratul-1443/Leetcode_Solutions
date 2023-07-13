class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        h=[0]*(n+1)
        z=-1
        for i in nums:
            h[i]+=1
        for i in range(n+1):
            if h[i]==0:
                z=i
        return z