"""
There is a row of empty (.) and filled (x) seats. Find the minimum number of moves required to make the people sit together.

Constraints:
1 <= N <= 1e6

Example:
Input: "..x..x."
Output: 2

Explanation:
Either of the "x"s can move to the seat closest to the other one.
i.e., "..xx..." or "....xx."
"""

def seats(row: str) -> int:
    filled_seats = [ind for ind, val in enumerate(row) if val == "x"]
    min_moves = 0
    segment_start = filled_seats[len(filled_seats) // 2] # finding the median in the list
    for filled_seat in filled_seats:
        min_moves += abs(filled_seat - segment_start)
    return min_moves


print(seats("..x..x."))