class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        先用hash表统计s中每个字符出现的次数，显然如果字符c出现的次数小于k，c必然不在最长子串里面，
        根据这个特性可以将原始s分割成多个子串递归地求解问题，我们用一个split数组依次来存放每个分割点的索引，
        对每个分割区间同样求解该问题(多路的分治问题)，
        并取结果的最大值保存在变量ans中，此处有一个小trick（如果当前求解的子串长度比已存在的ans还要小，
        则没有必要求解该区间，这样可以减少不必要的计算），
        最后递归的结束点就是当前求解的字符串s符合最长子串的要求
        '''
        if len(s) < k:
            return 0

        count_dict = {}
        for c in s:
            count_dict[c] = count_dict.get(c, 0) + 1

        split_c = None
        for c, f in count_dict.items():
            if f < k:
                split_c = c

        if split_c is None:
            return len(s)

        strs = s.split(sep=split_c)

        max_len = 0
        for s_ in strs:
            max_len = max(max_len, self.longestSubstring(s_, k))

        return max_len


class Solution1:
    def longestSubstring(self, s, k):
        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


if __name__ == '__main__':
    res = Solution().longestSubstring(s = "ababbc", k = 2)
    print(res)
    pass