# 制約は-2^31 <= x <= 2^31 - 11なので文字列の長さとしては31なので全探索でも計算量的には問題なし
# O(N)で計算可能

# 回文ということは、前から読んでも後ろから読んでも同じということ
# なので、先頭からと末尾からを順番に比較し同一の文字列であることを証明できれば回文と言える


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_reverse_str = ''.join(list(reversed(list(str(x)))))
        if x_str == x_reverse_str:
            return True
        return False
