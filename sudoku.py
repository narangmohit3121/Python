from collections import OrderedDict


def find_grid(x, y):

    if x < 3 and y < 3:
        return 0
    elif x < 3 and (3 <= y < 6):
        return 1
    elif x < 3 and (6 <= y < 9):
        return 2
    elif (3 <= x < 6) and y < 3:
        return 3
    elif (3 <= x < 6) and (3 <= y < 6):
        return 4
    elif (3 <= x < 6) and (6 <= y < 9):
        return 5
    elif (6 <= x < 9) and y < 3:
        return 6
    elif (6 <= x < 9) and (3 <= y < 6):
        return 7
    else:
        return 8


def create_sudoku_grid(dimension):
    grid = OrderedDict()
    for i in range(dimension):
        for j in range(dimension):
            current_index = (i, j, find_grid(i, j))
            grid[current_index] = 0

    return grid


def is_valid(grid, current_index, val):
    x, y, g = current_index
    col = []
    row = []
    grid_of_index = []
    for (current_position, current_val) in grid.items():
        current_row, current_col, current_grid = current_position
        if current_col == y:
            col.append(current_val)
        if current_row == x:
            row.append(current_val)
        if current_grid == g:
            grid_of_index.append(current_val)
    print("Col is:", col)
    print("Row is:", row)
    print("Grid is:", grid_of_index)
    print("*"*10)
    if (val in col) or (val in row) or (val in grid_of_index):
        return False
    else:
        return True


sudoku = create_sudoku_grid(9)
# for current_key in sudoku.keys():
#     print(current_key)
sudoku[(0, 2, 0)] = 7
sudoku[(0, 3, 1)] = 9

sudoku[(1, 3, 1)] = 2
sudoku[(1, 4, 1)] = 4
sudoku[(1, 6, 2)] = 1
sudoku[(1, 7, 2)] = 9

sudoku[(2, 1, 0)] = 4
sudoku[(2, 4, 1)] = 8
sudoku[(2, 6, 2)] = 3
sudoku[(2, 8, 2)] = 5

sudoku[(3, 0, 3)] = 5
sudoku[(3, 1, 3)] = 9
sudoku[(3, 3, 4)] = 8

sudoku[(4, 0, 3)] = 7
sudoku[(4, 2, 3)] = 8
sudoku[(4, 6, 5)] = 2
sudoku[(4, 8, 5)] = 9

sudoku[(5, 4, 4)] = 3
sudoku[(5, 7, 5)] = 5

sudoku[(6, 0, 6)] = 9
sudoku[(6, 1, 6)] = 1
sudoku[(6, 3, 7)] = 4
sudoku[(6, 5, 7)] = 8
sudoku[(6, 6, 8)] = 6
sudoku[(6, 7, 8)] = 2
sudoku[(6, 8, 8)] = 3

sudoku[(7, 0, 6)] = 4
sudoku[(7, 1, 6)] = 7
sudoku[(7, 2, 6)] = 3
sudoku[(7, 3, 7)] = 6
sudoku[(7, 5, 7)] = 5
sudoku[(7, 6, 8)] = 9
sudoku[(7, 7, 8)] = 8

sudoku[(8, 2, 6)] = 2
sudoku[(8, 3, 7)] = 3
sudoku[(8, 5, 7)] = 1


def print_sudoku(grid_to_print):
    for (current_key, current_val) in grid_to_print.items():
        r, c, gr = current_key
        print(current_val, end=" ")
        # print(current_key)
        if (c+1) % 3 == 0:
            # print("  ", end="")
            print(" ", end="")
        if c == 8:
            print("")
        if c == 8 and (r + 1) % 3 == 0:
            print("")


print(is_valid(sudoku, (1, 1, 1), 1))


def is_sudoku_solved(grid):
    for key in grid:
        if grid[key] == 0:
            return False
    return True


def solve_sudoku_puzzle(is_solved, sudoku_grid):
    print("-"*50)
    if is_solved:
        return [True, sudoku_grid]
    else:
        position_to_fill = None
        for key in sudoku_grid:
            # print(key)
            if sudoku_grid[key] == 0:
                position_to_fill = key
                break
        can_fill_current_position = False
        for value in range(1, 10):

            is_current_value_valid = is_valid(sudoku_grid, position_to_fill, value)
            if is_current_value_valid:
                print("*"*10)
                print(f'Entering value for {position_to_fill}: {value}')
                sudoku_grid[position_to_fill] = value
                print_sudoku(sudoku_grid)
                is_sudoku_filled = is_sudoku_solved(sudoku_grid)
                if not is_sudoku_filled:
                    result = solve_sudoku_puzzle(False, sudoku_grid)
                    # print(result[0], position_to_fill, value, " :", i)
                    can_fill_with_current_value = result[0]
                    if can_fill_with_current_value:
                        return [True, sudoku_grid]
                    else:
                        sudoku_grid[position_to_fill] = 0
                        continue
                else:
                    return [True, sudoku_grid]

            else:
                continue

        if not can_fill_current_position:
            return [False, sudoku_grid]


print(solve_sudoku_puzzle(False, sudoku))