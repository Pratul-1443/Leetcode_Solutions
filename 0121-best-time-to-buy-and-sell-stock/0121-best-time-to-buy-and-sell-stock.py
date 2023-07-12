class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans=0
        ptr=float("inf")
        for i in range(len(prices)):
            if prices[i] < ptr:
                ptr=prices[i]
                
            ans=max(ans,prices[i]-ptr)
        return ans