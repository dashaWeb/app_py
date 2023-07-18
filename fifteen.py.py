

# import msvcrt



# while True:
#     key = msvcrt.getch()
#     print(ord(key))
#     if ord(key) == 27:
#         break


# import random
# size = 4
# def createBoard():
#     mixboard = [i for i in range(1,size*size)]
#     random.shuffle(mixboard)
#     mixboard.append(0)
#     return [mixboard[i:i+size] for i in range(0,size*size,size)]



import random
import msvcrt

def create_board(size):
    numbers = list(range(1, size*size))
    numbers.append(None) 
    random.shuffle(numbers)
    board = [numbers[i:i+size] for i in range(0, size*size, size)]
    blank_row, blank_col = find_blank(board)
    last_row, last_col = size - 1, size - 1
    board[blank_row][blank_col], board[last_row][last_col] = board[last_row][last_col], board[blank_row][blank_col]

    return board

def print_board(board):
    size = len(board)
    border = '———' * size
    for i, row in enumerate(board):
        if i == 0:
            print(border)
        print('│', end='')
        for num in row:
            if num is not None:
                print(str(num).rjust(2), end='│')
            else:
                print('  ', end='│')
        print()
        print(border)

def find_blank(board):
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] is None:
                return i, j

def is_valid_move(board, move):
    blank_row, blank_col = find_blank(board)
    return move in ["w", "a", "s", "d"] and \
           (move == "w" and blank_row > 0 or move == "a" and blank_col > 0 or move == "s" and blank_row < len(board) - 1 or move == "d" and blank_col < len(board) - 1)

def perform_move(board, move):
    if not is_valid_move(board, move):
        return False
    
    blank_row, blank_col = find_blank(board)
    if move == "w":
        board[blank_row][blank_col], board[blank_row - 1][blank_col] = board[blank_row - 1][blank_col], board[blank_row][blank_col]
    elif move == "a":
        board[blank_row][blank_col], board[blank_row][blank_col - 1] = board[blank_row][blank_col - 1], board[blank_row][blank_col]
    elif move == "s":
        board[blank_row][blank_col], board[blank_row + 1][blank_col] = board[blank_row + 1][blank_col], board[blank_row][blank_col]
    elif move == "d":
        board[blank_row][blank_col], board[blank_row][blank_col + 1] = board[blank_row][blank_col + 1], board[blank_row][blank_col]
    return True

def is_solved(board):
    size = len(board)
    return all(board[i][j] == i*size + j + 1 for i in range(size) for j in range(size - 1)) and board[size - 1][size - 1] is None

def get_key_press():
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            return key.decode().lower()

def main():
    size = 4
    board = create_board(size)

    print("---Welcome---")

    while not is_solved(board):
        print("\n")
        print_board(board)
        move = get_key_press()
        if move == 'q':
            print("\nГра закінчена")
            return
        elif move in ["w", "a", "s", "d"]:
            if perform_move(board, move):
                print("\nХід зроблено")
            else:
                print("\nНевірний хід")
        else:
            print("\nEror. Використовуйте (w, a, s, d або q для виходу)")

    print("\nYou win !!!")

if __name__ == "__main__":
    main()

