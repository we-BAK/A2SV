class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        count=0
        for i in range(len(seats)):
            if seats[i]!=students[i]:
                count+=abs(seats[i]-students[i])
        return count