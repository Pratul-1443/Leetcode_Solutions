class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(0, len(times)):
            times[i].append(i)

        times.sort()
        
        seats = []
        
        for friend in times:
            i = 0
            if len(seats) == 0:
                seats.append(friend[1])
            else:
                while i < len(seats) and friend[0] < seats[i]:
                    i += 1
                if i < len(seats):
                    seats[i] = friend[1]
                else:
                    seats.append(friend[1])
            if friend[2] == targetFriend:
                return i

        return 0