import random


class Sudoku():

    def __init__(self):
        self.origin_board = [[0 for j in range(0,9)] for i in range(0,9)]
        self.board = [[0 for j in range(0,9)] for i in range(0,9)]
        self.row = [[0 for j in range(0,10)] for i in range(0,10)]
        self.col = [[0 for j in range(0,10)] for i in range(0,10)]
        self.diag = [[0 for j in range(0,10)] for i in range(0,10)]
        self.terminate_flag = False

        self.__board_init()

    def __board_init(self):
        seq_diag = [0,4,8]
        for offset in range(0,9,3):
            seq = [i for i in range(1,10)]
            random.shuffle(seq)
            for idx in range(0,9):
                i,j = idx//3,idx%3
                self.row[offset+i][seq[idx]] = 1
                self.col[offset+j][seq[idx]] = 1
                k = seq_diag[offset//3]
                self.diag[k][seq[idx]] = 1
                self.origin_board[offset+i][offset+j] = seq[idx]

    def __clean(self):
        self.origin_board = [[0 for j in range(0,9)] for i in range(0,9)]
        self.board = [[0 for j in range(0,9)] for i in range(0,9)]
        self.row = [[0 for j in range(0,10)] for i in range(0,10)]
        self.col = [[0 for j in range(0,10)] for i in range(0,10)]
        self.diag = [[0 for j in range(0,10)] for i in range(0,10)]
        self.terminate_flag = False

    def __make_sudoku(self, k):

        if self.terminate_flag == True:
            return True

        if k > 80:
            for i in range(0,9):
                for j in range(0,9):
                    self.board[i][j] = self.origin_board[i][j]
            self.terminate_flag = True
            return True

        i,j = k//9,k%9
        start_num = random.randint(1,9)

        if self.origin_board[i][j] != 0:
            self.__make_sudoku(k+1)

        for m in range(1,10):
            m = 1 + (m + start_num)%9
            d = (i//3)*3 + (j//3)
            if self.row[i][m] == 0 and self.col[j][m] == 0 and self.diag[d][m] == 0:
                self.row[i][m],self.col[j][m],self.diag[d][m] = 1,1,1
                self.origin_board[i][j] = m
                self.__make_sudoku(k+1)
                self.row[i][m],self.col[j][m],self.diag[d][m] = 0,0,0
                self.origin_board[i][j] = 0
    
    def __sudoku_check(self, puzzle):

        if puzzle != 9 or 

        for i in range(0,9):
            for j in range(0,9):
                k = (i//3)*3 + (j//3)
                num = puzzle[i][j]
                print(i,j,k,num)
                self.row[i][num]+=1
                self.col[j][num]+=1
                self.diag[k][num]+=1
        
        for idx in range(0,9):
            for num in range(1,10):
                if self.row[idx][num]!=1 or self.col[idx][num]!=1 or self.diag[idx][num]!=1:
                    return False
        
        return True

    def generate_puzzle(self):
        self.__clean()
        self.__make_sudoku(0)
        return self.board
    
    def sudoku_check(self,puzzle):
        self.__clean()
        return self.__sudoku_check(puzzle)