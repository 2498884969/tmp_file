# coding: utf-8
# n皇后
from typing import List
from pprint import pprint


class Solution:

    def __init__(self):
        self.res = []
        pass

    def solveNQueens(self, n: int) -> List[List[str]]:

        self.backtrack([(['.']*n)[:] for i in range(n)], 0, n)
        return self.res

    def backtrack(self, path: List[List[str]], row: int, n: int):

        # 终止条件-终止的时候进行字符串拼接
        if row == n:
            self.res.append([''.join(chars) for chars in path])
            return

        row_ = path[row]
        for i in range(n):
            # 选择
            row_[i] = 'Q'
            if self.is_valid(path, row, i):
                self.backtrack(path, row + 1, n)
            # 撤销选择
            row_[i] = '.'

    def is_valid(self, path: List[List[str]], row, col) -> bool:
        # path 为完整的图
        # n
        # 对角线关系  正对角线相减为常数 反对角线相加为常数
        # 有表达式的地方要注意边界
        n = len(path)
        # 左上角   从左向右推
        row_sub_col = row - col
        for i in range(row):
            if (0 <= i-row_sub_col < n) and path[i][i-row_sub_col] == 'Q':
                return False

        # 右上角   从左向右推
        row_add_col = row + col
        for i in range(row):
            if (0 <= row_add_col-i < n) and path[i][row_add_col-i] == 'Q':
                return False

        # 纵向校验
        for i in range(row):
            if path[i][col] == 'Q':
                return False
        # 返回正确结果
        return True


if __name__ == '__main__':
    res = Solution().solveNQueens(4)
    pprint(res)
