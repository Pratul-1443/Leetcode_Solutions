class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=0
        p=0
        high=len(nums)-1
        while(p<=high):
            if nums[p]==2:
                nums[high],nums[p]=nums[p],nums[high]
                high-=1
            elif nums[p]==0:
                nums[low],nums[p]=nums[p],nums[low]
                low+=1
                p+=1
            elif nums[p]==1:
                p+=1
        nums
            
            