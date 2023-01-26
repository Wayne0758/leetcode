class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        n=int(len(students))
        for j in range(n):
            for i in range(len(students)):
                if students[0]==sandwiches[0]:
                    students=students[1:]
                    sandwiches=sandwiches[1:]
                    break
                else:
                    students=students[1:]+[students[0]]
        return len(students)
