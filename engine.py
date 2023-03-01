import copy
import time


class Board():
    def __init__(self, board=None, player=1, look_up_table=None):
        if board is None:
            self.board = [
                # 0   1   2   3   4   5   6   7
                [0, -1,  0, -1,  0, -1,  0, -1],  # 0
                [-1, 0, -1,  0, -1,  0, -1, 0],  # 1
                [0, -1,  0, -1,  0, -1,  0, -1],  # 2
                [0,  0,  0,  0,  0,  0,  0,  0],  # 3
                [0,  0,  0,  0,  0,  0,  0,  0],  # 4
                [+1, 0, +1,  0, +1,  0, +1, 0],  # 5
                [0, +1,  0, +1,  0, +1,  0, +1],  # 6
                [+1, 0, +1,  0, +1,  0, +1,  0]  # 7
            ]
        else:
            self.board = copy.deepcopy(board)

        if look_up_table is None:
            self.look_up_table = dict()
        else:
            self.look_up_table = look_up_table

        self.turn = player  # black starts

    def _convert(self, x):
        if x == -1:
            return "x"
        elif x == 1:
            return "o"
        elif x == 0:
            return " "
        elif x == -2:
            return "X"
        elif x == 2:
            return "O"
        else:
            return "E"


    def _hash_pos(self):
        result = ""
        for i in range(8):
            for j in range(8):
                result += self._convert(self.board[i][j])
        return result


    # * prints a more human friendly board representation
    def display_board(self):
        #                                0                                1                                2                                3                               4                               5                               6                               7
        print(f"{self._convert(self.board[0][0])}|{self._convert(self.board[0][1])}|{self._convert(self.board[0][2])}|{self._convert(self.board[0][3])}|{self._convert(self.board[0][4])}|{self._convert(self.board[0][5])}|{self._convert(self.board[0][6])}|{self._convert(self.board[0][7])}")
        print("----------------")
        print(f"{self._convert(self.board[1][0])}|{self._convert(self.board[1][1])}|{self._convert(self.board[1][2])}|{self._convert(self.board[1][3])}|{self._convert(self.board[1][4])}|{self._convert(self.board[1][5])}|{self._convert(self.board[1][6])}|{self._convert(self.board[1][7])}")
        print("----------------")
        print(f"{self._convert(self.board[2][0])}|{self._convert(self.board[2][1])}|{self._convert(self.board[2][2])}|{self._convert(self.board[2][3])}|{self._convert(self.board[2][4])}|{self._convert(self.board[2][5])}|{self._convert(self.board[2][6])}|{self._convert(self.board[2][7])}")
        print("----------------")
        print(f"{self._convert(self.board[3][0])}|{self._convert(self.board[3][1])}|{self._convert(self.board[3][2])}|{self._convert(self.board[3][3])}|{self._convert(self.board[3][4])}|{self._convert(self.board[3][5])}|{self._convert(self.board[3][6])}|{self._convert(self.board[3][7])}")
        print("----------------")
        print(f"{self._convert(self.board[4][0])}|{self._convert(self.board[4][1])}|{self._convert(self.board[4][2])}|{self._convert(self.board[4][3])}|{self._convert(self.board[4][4])}|{self._convert(self.board[4][5])}|{self._convert(self.board[4][6])}|{self._convert(self.board[4][7])}")
        print("----------------")
        print(f"{self._convert(self.board[5][0])}|{self._convert(self.board[5][1])}|{self._convert(self.board[5][2])}|{self._convert(self.board[5][3])}|{self._convert(self.board[5][4])}|{self._convert(self.board[5][5])}|{self._convert(self.board[5][6])}|{self._convert(self.board[5][7])}")
        print("----------------")
        print(f"{self._convert(self.board[6][0])}|{self._convert(self.board[6][1])}|{self._convert(self.board[6][2])}|{self._convert(self.board[6][3])}|{self._convert(self.board[6][4])}|{self._convert(self.board[6][5])}|{self._convert(self.board[6][6])}|{self._convert(self.board[6][7])}")
        print("----------------")
        print(f"{self._convert(self.board[7][0])}|{self._convert(self.board[7][1])}|{self._convert(self.board[7][2])}|{self._convert(self.board[7][3])}|{self._convert(self.board[7][4])}|{self._convert(self.board[7][5])}|{self._convert(self.board[7][6])}|{self._convert(self.board[7][7])}")
        print("----------------")

    # * returns a list of tuples of all the available moves for a given square on the board

    def getMoves(self, x, y):
        moves = []
        # check all the empty squares that are on the board and can be accessed from (x, y)
        # if self.turn == -1: white to move and
        # if the piece on (x, y) is a man or is a king (kings can move like man but men cant move like kings)
        if self.board[x][y] in (self.turn, 2*self.turn):
            # to the right diagnoally (up if black, down if white)
            # check if target square is on the board
            if (x-self.turn) in range(8) and (y+1) in range(8):
                # check if target square is empty
                if self.board[x-self.turn][y+1] == 0:
                    moves.append((x-self.turn, y+1))
            # to the left diagnoally (up if black, down if white)
            # check if target square is on the board
            if (x-self.turn) in range(8) and (y-1) in range(8):
                # chcek if target square is empty
                if self.board[x-self.turn][y-1] == 0:
                    moves.append((x-self.turn, y-1))
        # if the piece on (x, y) is a king it can move backwards
        if self.board[x][y] == 2*self.turn:
            # to the right diagonally (down if black, up if white)
            # check if target square is on the board
            if (x+self.turn) in range(8) and (y+1) in range(8):
                # check if target square is empty
                if self.board[x+self.turn][y+1] == 0:
                    moves.append((x+self.turn, y+1))
            # check if target square is on the board
            if (x+self.turn) in range(8) and (y-1) in range(8):
                # check if target square is empty
                if self.board[x+self.turn][y-1] == 0:
                    moves.append((x+self.turn, y-1))
        return moves

    # * returns a list of tuples of all the available captures (jumps) for a given square on the board

    def getJumps(self, x, y):
        jumps = []
        # if the piece on (x, y) is a man or a king
        if self.board[x][y] in (self.turn, 2*self.turn):
            # to the right diagonally move 2
            if (x-2*self.turn) in range(8) and (y+2) in range(8):
                # check if jumped over square is occupied by opponent piece and if the next square is empty
                if self.board[x-self.turn][y+1] == -self.turn and self.board[x-2*self.turn][y+2] == 0:
                    jumps.append((x-2*self.turn, y+2))

            # to the left diagonally move 2
            if (x-2*self.turn) in range(8) and (y-2) in range(8):
                # check if jumped over square is occupied by opponent piece
                if self.board[x-self.turn][y-1] == -self.turn and self.board[x-2*self.turn][y-2] == 0:
                    jumps.append((x-2*self.turn, y-2))

        # if the piece on (x, y) is a king
        if self.board[x][y] == 2*self.turn:
            if (x+2*self.turn) in range(8) and (y+2) in range(8):
                if self.board[x+self.turn][y+1] == -1*self.turn and self.board[x+2*self.turn][y+2] == 0:
                    jumps.append((x+2*self.turn, y+2))
            if (x+2*self.turn) in range(8) and (y-2) in range(8):
                if self.board[x+self.turn][y-1] == -1*self.turn and self.board[x+2*self.turn][y-2] == 0:
                    jumps.append((x+2*self.turn, y-2))
        return jumps

    # * validiates the input move, if its legal it updates the board accordingly

    def move(self, x, y, newX, newY, comp=False):
        # stores al the availeble jumps in a dictionary
        jumpers = dict()

        # generate all possible captures
        for i in range(8):
            for j in range(8):
                if len(self.getJumps(x, y)):
                    jumpers[(i, j)] = self.getJumps(i, j)

        # if there are available captures
        if len(jumpers) > 0:
            # print(jumpers)
            if (newX, newY) in jumpers[(x, y)]:
                self.board[x][y] = 0
                self.board[newX][newY] = self.turn
                self.board[int((x+newX)/2)][int((y+newY)/2)] = 0

                self.makeKing()

                # print(self.getJumps(newX, newY))
                if len(self.getJumps(newX, newY)) == 1:
                    self.move(newX, newY, self.getJumps(newX, newY)[0][0], self.getJumps(newX, newY)[0][1])
                elif len(self.getJumps(newX, newY)) == 2:
                    if not comp:
                        self.display_board()
                        direction = str(input("You have two possible captures, would you like to go 'right' or 'left'? "))
                        for i in range(10):
                            if direction == 'right':
                                self.move(newX, newY, self.getJumps(newX, newY)[0][0], self.getJumps(newX, newY)[0][1])
                                break
                            elif direction == 'left':
                                self.move(newX, newY, self.getJumps(newX, newY)[1][0], self.getJumps(newX, newY)[1][1])
                                break
                            else:
                                print("Not a valid direction, please enter 'left' or 'right'")
                    else:
                        pass
                else:
                    self.turn = -self.turn
            else:
                print("invalid move, must take a piece if able to")
        else:
            if (newX, newY) in self.getMoves(x, y):
                self.board[x][y] = 0
                self.board[newX][newY] = self.turn
                self.turn = -self.turn
                self.makeKing()
            else:
                print("invalid move, either there isnt a piece there or the piece cannot move to the given position")

    # * converts last row pieces to kings

    def makeKing(self):
        for i in range(8):
            if self.board[0][i] == +1:
                self.board[0][i] = +2
            if self.board[7][i] == -1:
                self.board[7][i] = -2

    # * if there is a winner returns self.turn else it returns 0

    def checkWinner(self):
        blacks = 0
        whites = 0
        blacks_moves = []
        whites_moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == -1:
                    whites_moves.append(self.getMoves(i, j))
                    whites += 1
                elif self.board[i][j] == 1:
                    blacks_moves.append(self.getMoves(i, j))
                    blacks += 1
        if blacks == 0 or (len(blacks_moves) == 0 and self.turn == 1):
            return -float('inf')
        elif whites == 0 or (len(whites_moves) == 0 and self.turn == -1):
            return float('inf')
        else:
            return 0

    # * returns a numeric value representing the board position
    # TODO add heatmap

    def utility(self):
        score = 0
        for i in range(8):
            for j in range(8):
                score += self.board[i][j]
        return score

    # * implementation of the minimax algorithm

    def minimax(self, depth, alpha, beta, player):
        if self.checkWinner():
            return self.checkWinner()

        if depth == 0:
            return self.utility()

        if player == 1:
            value = -float('inf')
        else:
            value = float('inf')

        jumps = dict()
        moves = dict()

        # generate all legal moves
        for i in range(8):
            for j in range(8):
                if jump := self.getJumps(i, j):
                    jumps[(i, j)] = jump
                if move := self.getMoves(i, j):
                    moves[(i, j)] = move

        if jumps:
            for key in jumps:
                for val in jumps[key]:
                    child = Board(board=self.board, player=player, look_up_table=self.look_up_table)
                    child.move(key[0], key[1], val[0], val[1], comp=True)
                    if (hashed_pos := child._hash_pos()) in child.look_up_table:
                        score = child.look_up_table[hashed_pos]
                    else:
                        score = child.minimax(depth-1, alpha, beta, -1*player)
                        child.look_up_table[hashed_pos] = score

                    if player == 1:
                        if score > value:
                            value = score
                        if value > beta:
                            break
                        alpha = max(alpha, value)
                    elif player == -1:
                        if score < value:
                            value = score
                        if value < alpha:
                            break
                        beta = min(beta, value)
        elif moves:
            for key in moves:
                for val in moves[key]:
                    child = Board(board=self.board, player=player, look_up_table=self.look_up_table)
                    child.move(key[0], key[1], val[0], val[1], comp=True)
                    if (hashed_pos := child._hash_pos()) in child.look_up_table:
                        score = child.look_up_table[hashed_pos]
                    else:
                        score = child.minimax(depth-1, alpha, beta, -1*player)
                        child.look_up_table[hashed_pos] = score

                    if player == 1:
                        if score > value:
                            value = score
                        if value > beta:
                            break
                        alpha = max(alpha, value)
                    elif player == -1:
                        if score < value:
                            value = score
                        if value < alpha:
                            break
                        beta = min(beta, value)

        return value

    # * returns the best move according to the minimax algorithm
    # TODO
    
    def get_best_move(self, depth, player):
        best_move = (-1, -1, -1, -1)

        if player == 1:
            value = -float('inf')
        else:
            value = float('inf')

        moves = dict()
        jumps = dict()

        for i in range(8):
            for j in range(8):
                if jump := self.getJumps(i, j):
                    jumps[(i, j)] = jump
                if move := self.getMoves(i, j):
                    moves[(i, j)] = move

        if jumps:
            for key in jumps:
                for val in jumps[key]:
                    child = Board(board=self.board, player=player)
                    child.move(key[0], key[1], val[0], val[1], comp=True)
                    curr_move = (key[0], key[1], val[0], val[1])
                    score = child.minimax(depth-1, -float('inf'), float('inf'), -1*player)

                    if player == 1:
                        if score > value:
                            value = score
                            best_move = curr_move
                    elif player == -1:
                        if score < value:
                            value = score
                            best_move = curr_move
        
        elif moves:
            for key in moves:
                for val in moves[key]:
                    child = Board(board=self.board, player=player)
                    child.move(key[0], key[1], val[0], val[1], comp=True)
                    score = child.minimax(depth-1, -float('inf'), float('inf'), -1*player)
                    curr_move = (key[0], key[1], val[0], val[1])

                    if player == 1:
                        if score > value:
                            value = score
                            best_move = curr_move
                    elif player == -1:
                        if score < value:
                            value = score
                            best_move = curr_move

        return best_move



def main():
    board = Board()
    while True:
        board.display_board()
        # t1 = time.time()
        # print(f'minimax: {board.minimax(4, 1)}')
        # print(f'it took {time.time() - t1} seconds to run')
        t2 = time.time()
        print(f'best_move: {board.get_best_move(6, 1)}')
        print(f'it took {time.time() - t2} seconds to run')
        print(f'utility: {board.utility()}')
        print(f"turn: {board._convert(board.turn)}")
        x = int(input("Enter vertical cooardinate of the piece you wish to move "))
        y = int(input("Enter horizontal cooardinate of the piece you wish to move "))
        newX = int(input("Enter vertical cooardinate of the spot you wish to move to "))
        newY = int(input("Enter horizontal cooardinate of the spot you wish to move to "))

        board.move(x, y, newX, newY)

        if board.checkWinner() == float('inf'):
            print("Black won")
            break
        elif board.checkWinner() == -float('inf'):
            print("White won")
            break

    # nagyon szeretem a petyit


if __name__ == "__main__":
    main()
