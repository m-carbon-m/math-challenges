from random import randint

#Funktion 1
def make_random_move(positions):
    while True:
        position = randint(0,8)
        if positions[position] == " ":
            positions[position] = "O"
            return position

#Funktion 2
def make_good_move(positions, move_player_1, move_KI):
    position = is_winning_move(positions, move_KI)
    if position is not None:
        return position
    position = is_winning_move(positions, move_player_1)
    if position is not None:
        return position
    return make_random_move(positions)

#Funktion 3 - Alternativ
def is_winning_move(positions, move):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Zeilen
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Spalten
        [0, 4, 8], [2, 4, 6]              # Diagonalen 
    ]
    for combination in winning_combinations:
        if positions[combination[0]] == " " and positions[combination[1]] == move and positions[combination[2]] == move:
            positions[combination[0]] = "O"
            return combination[0]
        if positions[combination[0]] == move and positions[combination[1]] == " " and positions[combination[2]] == move:
            positions[combination[1]] = "O"
            return combination[1]
        if positions[combination[0]] == move and positions[combination[1]] == move and positions[combination[2]] == " ":
            positions[combination[2]] = "O"
            return combination[2]



