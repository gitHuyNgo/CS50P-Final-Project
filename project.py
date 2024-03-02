def main():
    print('Welcome to Sudoku Solver!')
    print('Enter your Sudoku board (9x9), use 0 to represent empty cells:')

    board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)

    print('\nSudoku puzzle:')
    display_board(board)

    if solve(board):
        print('\nSolution:')
        display_board(board)
    else:
        print('\nNo solution exists for the given Sudoku puzzle.')

def display_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end = '')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end = '')


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

if __name__ == "__main__":
    main()


