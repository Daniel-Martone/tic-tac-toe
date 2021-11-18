def heading(msg):
    print('-=-'*10)
    print(msg.center(30))
    print('-=-'*10)


def readint(msg = 'Number: ', errormsg= 'ERROR', max = 0, min = 0):
    while True:
        while True:
            try:
                num = int(input(msg))
            except:
                print(errormsg)
            else:
                break
        if num <= max and num >= min and max != 0:
            break
        else:
            print(errormsg)
    return num

class Board:
    def __init__(self, table):
        self.table = table
# ---------------------------
# ---------------------------
    def show(self):
        print('\n'*20)
        print('-=-'*10)
        print(f'''
 {self.table[0]} | {self.table[1]} | {self.table[2]}
-----------
 {self.table[3]} | {self.table[4]} | {self.table[5]}
-----------
 {self.table[6]} | {self.table[7]} | {self.table[8]}
        ''')
        print('-=-'*10)
# ---------------------------
# ---------------------------
    def add(self, player, square):
        if self.table[square-1] == ' ':
            self.table[square-1] = player.symbol 


class Player:
    def select_symbol(self, msg):
        while True:
            symbol = input(msg)
            if symbol in ['', ' '] or len(symbol) != 1:
                print('Invalid symbol, make sure that it has 1 character!')
            else:
                break
        self.symbol = symbol
# ---------------------------
# ---------------------------
    def make_play(self, name, board):
        while True:
            square = readint(f'{name} Square: ', 'Select a valid square (1-9)', max = 9, min = 1)
            if board.table[square-1] != ' ':
                print('Select a valid square (Not used yet)')
            else:
                break
        board.add(self, square)
# ---------------------------
# ---------------------------
    def check_win(self, board):
        wincons = [
[0, 1, 2], [3, 4, 5], [6, 7, 8], 
[0, 3, 6], [1, 4, 7], [2, 5, 8],
[0, 4, 8], [2, 4, 6]]
        for c in wincons:
            if board.table[c[0]] == board.table[c[1]] == board.table[c[2]] == self.symbol:
                return True
        return False