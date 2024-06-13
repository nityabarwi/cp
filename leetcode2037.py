def minMovesToSeat(seats, students):
        seats.sort()
        students.sort()
        moves = 0
        for seat, student in zip(seats, students):
            moves += abs(seat - student)
        return moves


