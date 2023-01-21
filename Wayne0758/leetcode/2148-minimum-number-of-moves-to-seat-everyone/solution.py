class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        a=0
        for i in range(len(seats)):
            b=abs(seats[i]-students[i])
            a+=b
        return a
