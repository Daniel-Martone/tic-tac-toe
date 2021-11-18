from utilities import *

table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board = Board(table)

p1 = Player()
p2 = Player()

print('-=-'*10)
p1.select_symbol('Player 1 symbol: ')
p2.select_symbol('Player 2 symbol: ')

while True:
    board.show()

    p2win = p2.check_win(board)
    if p2win:
        heading('PLAYER 2 WINS!')
        break

    p1.make_play('Player 1', board)
    board.show()

    p1win = p1.check_win(board)
    if p1win:
        heading('PLAYER 1 WINS!')
        break

    p2.make_play('Player 2', board)
print('Thanks for playing!')
