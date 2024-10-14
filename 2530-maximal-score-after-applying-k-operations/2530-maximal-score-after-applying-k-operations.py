class Solution:
    def maxKelements(self, nums, k):
        pq = [-num for num in nums]
        heapq.heapify(pq)
        score = 0

        for _ in range(k):
            max_val = -heapq.heappop(pq)
            score += max_val
            heapq.heappush(pq, -math.ceil(max_val / 3.0))

        return score