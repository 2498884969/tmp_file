from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # 1. 构建结果集哈希表 AB{sum, f} CD{sum, f}
        # 2. 便利  COUNT += AB[V]*CD[-V]
        ab = {}
        for a in A:
            for b in B:
                ab[a+b] = ab.get(a+b, 0) + 1
        cd = {}
        for c in C:
            for d in D:
                cd[c + d] = cd.get(c + d, 0) + 1

        count = 0
        for v, f in ab.items():
            if -v not in cd:
                continue
            count += f * cd.get(-v, 0)
        return count


if __name__ == '__main__':
    res = Solution().fourSumCount(
        A=[1, 2],
    B=[-2, -1],
    C=[-1, 2],
    D=[0, 2],
    )
    print(res)
