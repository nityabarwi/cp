def minMovesToSeat(seats, students):
        seats.sort()
        students.sort()
        moves = 0
        for seat, student in zip(seats, students):
            moves += abs(seat - student)
        return moves

seats1 = [3,1,5]
students1 = [2,7,4]
print(minMovesToSeat(seats1, students1)              # Output = 4
