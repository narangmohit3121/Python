
def generate_pos_id(row, col, board_size):
    return (row*board_size) + col


def legal_moves(current_row, current_col, board_size):

    def is_valid_move(r, c, size_of_board):
        if 0 <= r < size_of_board and 0 <= c < size_of_board:
            return True
        else:
            return False

    new_moves = []
    move_offsets = [(1, 2),
                    (-1, 2),
                    (1, -2),
                    (-1, -2),
                    (2, 1),
                    (-2, 1),
                    (2, -1),
                    (-2, -1)]

    for row_move, col_move in move_offsets:
        new_move = (current_row + row_move, current_col + col_move)
        is_current_move_valid = is_valid_move(*new_move, board_size)
        if is_current_move_valid:
            new_moves.append(new_move)
    return new_moves


def generate_knight_graph(board_size):
    graph = {}
    for row in range(board_size):
        for col in range(board_size):
            current_pos_id = generate_pos_id(row, col, board_size)
            new_positions = legal_moves(row, col, board_size)
            set_of_positions = set()
            for new_position in new_positions:
                new_row, new_col = new_position
                set_of_positions.add(generate_pos_id(new_row, new_col, board_size))
            graph[current_pos_id] = set_of_positions
    return graph


def knight_tour_path(graph, current_pos, current_depth, limit, path=[]):
    path.append(current_pos)
    done = False
    if current_depth < limit:
        valid_moves = list(graph[current_pos])
        i = 0
        while i < len(valid_moves) and not done:
            new_pos = valid_moves[i]
            if new_pos not in path:
                done = knight_tour_path(graph, new_pos, current_depth + 1, limit, path)
            i += 1
        if not done:
            path.pop()
    else:
        done = True
    print(path)
    print(current_depth)
    return done


print(generate_knight_graph(6))
print(knight_tour_path(generate_knight_graph(6), 3, 0, 35))
