# minesweeper.py

def is_valid_position(grid, row, col):
    """
    Check if a given row and column are within the grid boundaries.
    """
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def count_adjacent_mines(grid, current_row, current_col):
    """
    Count the number of mines (#) adjacent to a specific cell.
    Includes horizontal, vertical, and diagonal positions.
    """
    mine_count = 0

    # All 8 possible directions around a cell
    directions = [
        (-1, -1), (-1, 0), (-1, 1),   # NW, N, NE
        (0, -1),          (0, 1),    # W,     E
        (1, -1),  (1, 0),  (1, 1)     # SW, S, SE
    ]

    for row_offset, col_offset in directions:
        new_row = current_row + row_offset
        new_col = current_col + col_offset

        if is_valid_position(grid, new_row, new_col):
            if grid[new_row][new_col] == "#":
                mine_count += 1

    return mine_count


def minesweeper(grid):
    """
    Takes a grid of '-' and '#' and returns a new grid
    where '-' is replaced with the number of adjacent mines.
    """
    result = []

    for row_index, row in enumerate(grid):
        new_row = []

        for col_index, cell in enumerate(row):

            if cell == "#":
                new_row.append("#")
            else:
                count = count_adjacent_mines(grid, row_index, col_index)
                new_row.append(count)

        result.append(new_row)

    return result


# --- Example Input --- #
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# --- Run Minesweeper Function --- #
output_grid = minesweeper(input_grid)

# --- Display Result --- #
for row in output_grid:
    print(row)
