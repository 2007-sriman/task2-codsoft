import math


board = [' ' for _ in range(9)]


def print_board():
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")


def check_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    return any(all(brd[i] == player for i in combo) for combo in win_conditions)

def is_draw(brd):
    return ' ' not in brd

def minimax(brd, depth, is_maximizing):
    if check_winner(brd, 'X'):
        return 1
    if check_winner(brd, 'O'):
        return -1
    if is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'X'


def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'O'. AI is 'X'.")
    print("Board positions are:")
    print("0 | 1 | 2\n--+---+--\n3 | 4 | 5\n--+---+--\n6 | 7 | 8\n")
    print_board()

    while True:
        
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'O'
        print_board()

        if check_winner(board, 'O'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI's move:")
        ai_move()
        print_board()

        if check_winner(board, 'X'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break


play_game()