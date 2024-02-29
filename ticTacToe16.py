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
#Delimitation de mon board et lorsque une position est déjà utilisé alors ce dernier ne peut être réutiliser
    
def bounds(user_input):
    if user_input > 256 or user_input < 1:
        print("###cette position n'existe pas dans la grille ")
        return False
    else: 
        return True
#lorsque une position est déjà utilisé alors ce dernier ne peut être réutiliser
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

####Verification lorsque il y un alignement "X" ou "O" horizontal, verticale ou oblique 
def check_winner(board):

#Vérification des lignes s'il y a un alignement verticale
    for row in board:
        if "XXXX" in "".join(row) or "OOOO" in "".join(row):
            return True

#Vérification des colonnes s'il y a un aligneemnt horizontal
    for col in range(len(board[0])):
        column_str = "".join([board[row][col] for row in range(len(board))])
        if "XXXX" in column_str or "OOOO" in column_str:
            return True

#Vérification des lignes diagonales s'il y a un alignement oblique en allant de haut en bas
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            diag_str = "".join([board[i + k][j + k] for k in range(4)])
            if "XXXX" in diag_str or "OOOO" in diag_str:
                return True

#Vérification des lignes diagonales s'il y a un alignement oblique en allant de bas en haut
    for i in range(3, len(board)):
        for j in range(len(board[0]) - 3):
            diag_str = "".join([board[i - k][j + k] for k in range(4)])
            if "XXXX" in diag_str or "OOOO" in diag_str:
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

    if check_winner(board):
        print_board(board)
        print(f"Le joueur avec la valeur '{user_symbol}' a remporté la partie !")
        break
