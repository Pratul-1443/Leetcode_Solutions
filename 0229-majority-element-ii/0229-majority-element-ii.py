from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        z=[]
        mini=(len(nums)//3)
        a=Counter(nums)
        for i,j in a.items():
            if j>mini:
                z.append(i)
        return z
 