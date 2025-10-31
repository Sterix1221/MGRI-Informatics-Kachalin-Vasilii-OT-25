def initialize_board():
    board = []
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i] += '#'
    return board


def display_board(board):
    print('  1 2 3')
    for i in range(3):
        print(f'{i + 1}', end=' ')
        for j in range(3):
            print(board[i][j], end=' ')
        print()
    print()


def make_move(board, row, col, player):
    if board[row][col] == '#':
        board[row][col] = player
        return True
    else:
        print('Эта ячейка занята!')
        return False


def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'
    

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '#':
            return board[i][0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '#':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != '#':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != '#':
        return board[0][2]
    return None

def is_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]:
                return False
    return True


def get_input(player):
    while True:
        player_row = input('Введите номер строки (1, 2, 3): ')
        player_col = input('Введите номер столбца (1, 2, 3): ')
        if not (player_row.isdigit()) or not (player_col.isdigit()):
            print('Введите целое число.')
            continue
        elif not (0 < int(player_row) < 4) and not (0 < int(player_col) < 4):
            print('Число вне диапазона.')
            continue
        else:
            return int(player_row) - 1, int(player_col) - 1 


def main():
    board = initialize_board()
    current_player = 'X'
    game_over = False
    winner = None

    while not game_over:
        display_board(board)
        row, col = get_input(current_player)

        if make_move(board, row, col, current_player):
            winner = check_winner(board)
            if winner:
                game_over = True
                display_board(board)
                print(f'Игрок {winner} выиграл!')
                break

            if is_draw(board):
                game_over = True
                display_board(board)
                print('Ничья')
                break

            current_player = switch_player(current_player)

main()

