def max_cells_captured(game_board):
    row = len(game_board)
    column = len(game_board[0])

    mahesh_captured = [[0] * column for _ in range(row)]
    suresh_captured = [[0] * column for _ in range(row)]

    # Mahesh checks down and right direction
    for i in range(row - 1, -1, -1):
        for j in range(column - 1, -1, -1):
            if game_board[i][j] == 1:
                mahesh_captured[i][j] = 1 + max(
                    mahesh_captured[i + 1][j] if i + 1 < row else 0,
                    mahesh_captured[i][j + 1] if j + 1 < column else 0
                )

    # Suresh checks up and left direction
    for i in range(row):
        for j in range(column):
            if game_board[i][j] == 1:
                suresh_captured[i][j] = 1 + max(
                    suresh_captured[i - 1][j] if i - 1 >= 0 else 0,
                    suresh_captured[i][j - 1] if j - 1 >= 0 else 0
                )

    # Print captured cell matrices
    print("Mahesh Captured Cells:")
    for row in mahesh_captured:
        print(row)

    print("Suresh Captured Cells:")
    for row in suresh_captured:
        print(row)

    return min(mahesh_captured[0][0], suresh_captured[0][0])

# Example usage
grid = [
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1]
]
# grid = [
#     [0,1,1],[1,1,0],[1,0,1]
# ]

result = max_cells_captured(grid)
print("Result:", result)