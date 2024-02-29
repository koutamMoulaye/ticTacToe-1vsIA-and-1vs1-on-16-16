import random

board = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def quit(user_input):
    if user_input.lower() == "q":
        print("\nMerci pour votre participation !!")
        return True
    else:
        return False

def check_input(user_input):
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    if not bounds(user_input):
        return False
    return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("#### ERREUR entrer une valeur valide")
        return False
    else:
        return True

def bounds(user_input):
    if user_input > 256 or user_input < 1:
        print("###cette position n'existe pas dans la grille ")
        return False
    else:
        return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("###Cette position est déjà utilisée")
        return True
    else:
        return False

def coordinates(user_input):
    row = int((user_input - 1) / 16)
    col = (user_input - 1) % 16
    return row, col

def ai_move(board):
    for row in range(16):
        for col in range(16):
            if board[row][col] == "-":
                board[row][col] = "O"  
                if check_winner(board, "O"):
                    board[row][col] = "-"
                    return row, col  # Renvoyer les coordonnées plutôt que l'indice unique
                board[row][col] = "-"

    for row in range(16):
        for col in range(16):
            if board[row][col] == "-":
                board[row][col] = "X"  
                if check_winner(board, "X"):
                    board[row][col] = "-"
                    return row, col  # Renvoyer les coordonnées plutôt que l'indice unique
                board[row][col] = "-"

    empty_slots = [(row, col) for row in range(16) for col in range(16) if board[row][col] == "-"]
    return random.choice(empty_slots)


def check_winner(board, symbol):
    for row in board:
        if f"{symbol * 4}" in "".join(row):
            return True

    for col in range(len(board[0])):
        column_str = "".join([board[row][col] for row in range(len(board))])
        if f"{symbol * 4}" in column_str:
            return True

    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            diag_str = "".join([board[i + k][j + k] for k in range(4)])
            if f"{symbol * 4}" in diag_str:
                return True
            diag_str = "".join([board[i + 3 - k][j + k] for k in range(4)])
            if f"{symbol * 4}" in diag_str:
                return True
    return False


while True:
    print_board(board)
    user_input = input("Veuillez entrer une position(1 à 256) de la valeur(O ou X) pour jouer ou 'q' pour quitter : ")
    if quit(user_input):
        break
    if not check_input(user_input):
        continue
    user_input = int(user_input)
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("#### Veuillez réessayer encore")
        continue
    user_symbol = input("Veuillez entrer la valeur (O ou X) pour la position sélectionnée : ").upper()
    board[coords[0]][coords[1]] = user_symbol

    if check_winner(board, user_symbol):
        print_board(board)
        print(f"Le joueur avec la valeur '{user_symbol}' a remporté la partie !")
        break

    ai_position = ai_move(board)
    board[ai_position[0]][ai_position[1]] = "O"  # Utilisation des coordonnées renvoyées par ai_move

    if check_winner(board, "O"):
        print_board(board)
        print(f"L'IA avec la valeur 'O' a remporté la partie !")
        break
