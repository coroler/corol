import copy
import sys

sys.setrecursionlimit(100000)

board = [[".", "7", "3", ".", "9", ".", ".", ".", "6"],
         [".", ".", ".", ".", "2", ".", ".", "4", "."],
         [".", ".", ".", ".", ".", "5", ".", "7", "."],
         [".", ".", ".", "6", "8", ".", ".", "1", "."],
         ["5", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", ".", ".", ".", "4", "6", ".", "."],
         ["2", ".", "9", ".", ".", ".", "7", ".", "."],
         ["7", ".", ".", "1", ".", ".", ".", ".", "8"],
         ["6", ".", ".", ".", ".", ".", ".", ".", "."]]


class Solution():
    def __init__(self):
        self.row = 0
        self.cloumn = 0
        self.complete_flg = False
        self.insert_flg_list = [[False for _ in range(9)] for _ in range(9)]
        self.count = 0

    def get_check_list(self, tmp_board):
        row_list = [num for num in tmp_board[self.row] if num != '.']
        cloumn_list = [nums[self.cloumn] for nums in tmp_board if nums[self.cloumn] != '.']
        row_num = self.row / 3
        cloumn_num = self.cloumn / 3
        square_list = list()
        for i in range(3):
            for j in range(3):
                if tmp_board[3 * row_num + i][3 * cloumn_num + j] != '.':
                    square_list.append(tmp_board[3 * row_num + i][3 * cloumn_num + j])

        num = tmp_board[self.row][self.cloumn]
        if num in row_list:
            row_list.remove(num)
        if num in cloumn_list:
            cloumn_list.remove(num)
        if num in square_list:
            square_list.remove(num)

        return row_list, cloumn_list, square_list
    
    def insert(self, board, tmp_board):
        self.count += 1
        import pdb
        pdb.set_trace()
        if self.complete_flg:
            return

        insert_flg = False

        if self.count >= 22760:
            for i in range(9):
                print tmp_board[i]

        row_list, cloumn_list, square_list = self.get_check_list(tmp_board)
        if self.count >= 22760:
            for i in range(9):
                print "=============================================="
                print row_list
                print cloumn_list
                print square_list
                print "=============================================="

        if board[self.row][self.cloumn] == '.':
            if tmp_board[self.row][self.cloumn] == '.':
                num = 0
            else:
                num = int(tmp_board[self.row][self.cloumn])
            while(num < 9):
                num += 1
                if str(num) not in row_list and str(num) not in cloumn_list and str(num) not in square_list:
                    insert_flg = True
                    break
            if not insert_flg:
                tmp_board[self.row][self.cloumn] = '.'
                while(not self.insert_flg_list[self.row][self.cloumn]):
                    self.cloumn -= 1
                    if self.cloumn == -1:
                        self.row -= 1
                        self.cloumn = 8
                    if self.row == -1:
                        break
                self.insert_flg_list[self.row][self.cloumn] = False
        else:
            self.cloumn += 1
            if self.cloumn == 9:
                self.row += 1
                self.cloumn = 0
            if self.row == 9:
                self.complete_flg = True
            self.insert(board, tmp_board)

        if insert_flg:
            tmp_board[self.row][self.cloumn] = str(num)
            self.insert_flg_list[self.row][self.cloumn] = True
            self.cloumn += 1
            if self.cloumn == 9:
                self.row += 1
                self.cloumn = 0
            if self.row == 9:
                self.complete_flg = True

        if not self.complete_flg:
            self.insert(board, tmp_board)
        
    def solution(self, board):
        tmp_board = copy.deepcopy(board)
        self.insert(board, tmp_board)
        return tmp_board, self.count


if __name__ == '__main__':
    result, count = Solution().solution(board)
    for i in range(9):
        print board[i]

    print "==============================================="

    for i in range(9):
        print result[i]

    print "==============================================="
    
    print count
