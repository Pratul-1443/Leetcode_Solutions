class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums)<target:
            return 0
        
        i=0
        j=0
        res=0
        temp=float("inf")
        n=len(nums)
        while(j<n):
            res+=nums[j]
            while(res>=target and i<=j):
                
                temp=min(temp,j-i+1)
                res-=nums[i]
                i+=1
            j+=1
        return temp
