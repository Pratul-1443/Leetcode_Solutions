class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        ele=None
        n=len(nums)
        for i in range(n):
            if c==0:
                c=1
                ele=nums[i]
            elif nums[i]==ele:
                c+=1
            else:
                c-=1
        cnt=0
        for i in range(n):
            if nums[i] ==ele:
                cnt+=1
        if cnt>n//2:
            return ele
        else:-1
                
