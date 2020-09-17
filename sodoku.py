import copy
import sys

sys.setrecursionlimit(10000)

board = [[".", "7", "3", ".", "9", ".", ".", ".", "6"],
         [".", ".", ".", ".", "2", ".", ".", "4", "."],
         [".", ".", ".", ".", ".", "5", ".", "7", "."],
         [".", ".", ".", "6", "8", ".", ".", "1", "."],
         ["5", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", ".", ".", ".", "4", "6", ".", "."],
         ["2", ".", "9", ".", ".", ".", "7", ".", "."],
         ["7", ".", ".", "1", ".", ".", ".", ".", "8"],
         ["6", ".", ".", ".", ".", ".", ".", ".", "."]]


class Solution(object):
    def __init__(self):
        self.row = 0
        self.cloumn = 0
        self.complete_flg = False
        self.insert_flg_list = [[False for _ in range(9)] for _ in range(9)]
        self.count = 0

    def get_check_list(self, board):
        row_list = [num for num in board[self.row] if num != '.']
        cloumn_list = [nums[self.cloumn] for nums in board if nums[self.cloumn] != '.']
        row_num = self.row / 3
        cloumn_num = self.cloumn / 3
        square_list = list()
        for i in range(3):
            for j in range(3):
                if board[3 * row_num + i][3 * cloumn_num + j] != '.':
                    square_list.append(board[3 * row_num + i][3 * cloumn_num + j])

        num = board[self.row][self.cloumn]
        if num in row_list:
            row_list.remove(num)
        if num in cloumn_list:
            cloumn_list.remove(num)
        if num in square_list:
            square_list.remove(num)

        return row_list, cloumn_list, square_list
    
    def insert(self, board, tmp_board):
        self.count += 1
        if self.complete_flg:
            return

        insert_flg = False

        row_list, cloumn_list, square_list = self.get_check_list(board)

        if tmp_board[self.row][self.cloumn] == '.':
            if board[self.row][self.cloumn] == '.':
                num = 0
            else:
                num = int(board[self.row][self.cloumn])
            while(num < 9):
                num += 1
                if str(num) not in row_list and str(num) not in cloumn_list and str(num) not in square_list:
                    insert_flg = True
                    break
            if not insert_flg:
                board[self.row][self.cloumn] = '.'
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
            return self.insert(board, tmp_board)

        if insert_flg:
            board[self.row][self.cloumn] = str(num)
            self.insert_flg_list[self.row][self.cloumn] = True
            self.cloumn += 1
            if self.cloumn == 9:
                self.row += 1
                self.cloumn = 0
            if self.row == 9:
                self.complete_flg = True

        if not self.complete_flg:
            return self.insert(board, tmp_board)

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        tmp_board = copy.deepcopy(board)
        self.insert(board, tmp_board)
        return tmp_board


if __name__ == '__main__':
    result = Solution().solveSudoku(board)
    print result
