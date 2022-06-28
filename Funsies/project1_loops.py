import copy

def count_none(lst):
    sum = 0
    for sublst in lst:
        for element in sublst:
            if element == None:
                sum += 1
    return sum

def valid_path(board, row, col):
    """Returns a list of valid moves for the Knight based on starting row and col"""
    valid_move_list = []
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        if 0 <= row + 2 < len(board) and 0 <= col + 1 < len(board[0]) and board[row + 2][col + 1] is None:
            valid_move_list.append((row + 2, col + 1))

        if 0 <= row + 2 < len(board) and 0 <= col - 1 < len(board[0]) and board[row + 2][col - 1] is None:
            valid_move_list.append((row + 2, col - 1))

        if 0 <= row - 2 < len(board) and 0 <= col + 1 < len(board[0]) and board[row - 2][col + 1] is None:
            valid_move_list.append((row - 2, col + 1))

        if 0 <= row - 2 < len(board) and 0 <= col - 1 < len(board[0]) and board[row - 2][col - 1] is None:
            valid_move_list.append((row - 2, col - 1))

        if 0 <= row + 1 < len(board) and 0 <= col + 2 < len(board[0]) and board[row + 1][col + 2] is None:
            valid_move_list.append((row + 1, col + 2))

        if 0 <= row - 1 < len(board) and 0 <= col + 2 < len(board[0]) and board[row - 1][col + 2] is None:
            valid_move_list.append((row - 1, col + 2))

        if 0 <= row + 1 < len(board) and 0 <= col - 2 < len(board[0]) and board[row + 1][col - 2] is None:
            valid_move_list.append((row + 1, col - 2))

        if 0 <= row - 1 < len(board) and 0 <= col - 2 < len(board[0]) and board[row - 1][col - 2] is None:
            valid_move_list.append((row - 1, col - 2))

    return valid_move_list


def find_tour(board, row, col):
    copy_board = [list(lst) for lst in board]
    copy_board[row][col] = 'V'
    start_row = row
    start_col = col
    if count_none(copy_board) == 0:
        return [(row, col)]

    elif count_none(copy_board) != 0 and len(valid_path(copy_board, row, col)) == 0:
        return None

    path = valid_path(copy_board, row, col)
    while len(path) >= 1:
        row, col = path[0]
        try_path = find_tour(copy_board, row, col)
        if try_path is None:
            path = path[1:]
        else:
            return [(start_row,start_col)] + try_path


board = [["B", None, None, None, "Q"],
                 [None, "N", "P", None, None],
                 [None, None, None, "P", None],
                 [None, None, None, None, None],
                 [None, "K", None, None, "R"]] 

print(count_none(board))
print(find_tour(board, 1, 1))
print(board)
