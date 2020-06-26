# coding:utf-8
# 全排列
from typing import List
from pprint import pprint


class Solution:

    def __init__(self):
        self.res = []
        pass

    def permute(self, nums: List[int]) -> List[List[int]]:

        self.backtrack([], nums)
        return self.res

    def backtrack(self, path: List[int], choice: List[int]):

        # 1. 终止条件
        if len(path) == len(choice):
            # 注意是复制
            self.res.append(path[:])
            return

        for v in choice:
            if v in path:
                continue
            # 2. 做选择
            path.append(v)
            # 3. 递归
            self.backtrack(path, choice)
            # 4. 撤销选择
            path.pop()


if __name__ == '__main__':
    res = Solution().permute([1, 2, 3])
    pprint(res)