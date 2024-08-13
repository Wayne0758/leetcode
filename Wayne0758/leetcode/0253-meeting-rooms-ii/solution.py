class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        rooms = defaultdict(int)
        rooms[0] = intervals[0][1]
        roomcount = 0
        for interval in intervals[1:]:
            flag = 0
            for i in rooms.keys():
                if interval[0]>=rooms[i]:
                    rooms[i] = interval[1]
                    flag=1
                    break
            if flag == 0:
                roomcount+=1
                rooms[roomcount] = interval[1]
        return roomcount+1
