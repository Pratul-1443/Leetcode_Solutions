class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        n=len(intervals)
        prev=intervals[0][1]
        ans=0
        for i in range(1,n):
            if intervals[i][0]>=prev:
                prev=intervals[i][1]
            else:
                ans+=1
        return ans
