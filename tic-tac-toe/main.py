import board as b
import KI

# Projekt : Tic-Tac-Toe

print('Spieler 1')
player_1 = input('Dein Name: ')
print(f'Spieler 2\nComputer')

positions = {
    0: " ", 1: " ", 2: " ",
    3: " ", 4: " ", 5: " ",
    6: " ", 7: " ", 8: " "
}
move_player_1 = 'X'
move_KI = 'O'

print(b.draw_board(positions))

while True:
    # Zug von Spieler 1
    position_player_1 = int(input(f'{player_1} wo möchtest du spielen? [0-8] '))

    if b.check_if_valid(position_player_1, move_player_1, positions):
        print(b.draw_board(positions))
    else:
        print(f"\nUngültige Eingabe!")
        continue
        
    winner = b.check_win_condition(positions, move_player_1, move_KI, player_1)
    print(b.scorecard(winner, player_1))
    if winner != 0:
        if input("Möchtest du noch einmal spielen? (ja/nein)").lower() != "ja":
            break
        else: 
            b.clear_board(positions)
            
    # Zug der KI        
    position_KI = KI.make_good_move(positions, move_player_1, move_KI)
    print(f"Der Computer spielt {position_KI}\n{b.draw_board(positions)}")

    winner = b.check_win_condition(positions, move_player_1, move_KI, player_1)
    print(b.scorecard(winner, player_1))
    if winner != 0:
        if input(f'\nMöchtest du noch einmal spielen? (ja/nein)').lower() != "ja":
            break
        else:
            print()
            b.clear_board(positions)
                                