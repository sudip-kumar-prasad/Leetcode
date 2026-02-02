class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        x = []
        for i in range(len(seats)):
            x.append(abs(seats[i] - students[i]))
        return sum(x)
        