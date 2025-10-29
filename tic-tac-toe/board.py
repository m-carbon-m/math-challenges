#Funktion 1 - Zeichnet das Spielfeld mit den aktuellen Positionen
def draw_board(positions):
    board = "\n"
    board += f" {positions[0]:^3} | {positions[1]:^3} | {positions[2]:^3} \n"
    board += "-----+-----+-----\n"
    board += f" {positions[3]:^3} | {positions[4]:^3} | {positions[5]:^3} \n"
    board += "-----+-----+-----\n"
    board += f" {positions[6]:^3} | {positions[7]:^3} | {positions[8]:^3} \n"
    board += "\n"
    return board

#Funktion 2 - Prüft, ob der Zug erlaubt ist, und speichert ihn, wenn ja
def check_if_valid(position, move, positions):
    if position in positions.keys() and positions[position] == " ":
        positions[position] = move
        return True
    else:
        return False

#Funktion 3 - Prüft, ob jemand gewonnen hat oder ob das Spiel unentschieden ist
def check_win_condition(positions, move_player_1, move_KI, player_1):
    if check_if_win(positions, move_player_1):
        print(f'Player {player_1} hat gewonnen!')
        return 1
    elif check_if_win(positions, move_KI): 
        print(f'Der Computer hat gewonnen!')
        return 2
    else: 
        for p in positions.values():
            if p == " ":        
                return 0
        return 3

#Funktion 4 - Prüft, ob drei gleiche Symbole zum Sieg führen
def check_if_win(positions, move):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Zeilen
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Spalten
        [0, 4, 8], [2, 4, 6]              # Diagonalen 
    ]
    for combination in winning_combinations:
        if positions[combination[0]] == move and positions[combination[1]] == move and positions[combination[2]] == move:
            return True
    return False

#Funktion 5 - Zeigt das Ergebnis oder ein Unentschieden an
def scorecard(winner, player_1):
    if winner == 0:
        return "" 
    else:
        print(f"{"-" * 30}\n{'SCOREBOARD':^30}\n{"-" * 30}")
        if winner == 3:
            return f'Unentschieden!\n{player_1}{"0":^5}\nComputer{"0":^5}\n{"-" * 30}'
        elif winner == 1:
            return f'{player_1}{'1':^5}\nComputer{'0':^5}\n{"-" * 30}'
        elif winner == 2:
            return f'{player_1}{'0':^5}\nComputer{'1':^5}\n{"-" * 30}'

#Funktion 6 - Setzt das Spielfeld zurück (alle Felder leer)
def clear_board(positions):
    for i in range(9):
        positions[i] = " "