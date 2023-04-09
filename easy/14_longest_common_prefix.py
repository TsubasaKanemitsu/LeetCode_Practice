from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 最小の長さを求める
        min_len = 10 ** 2
        for s in strs:
            min_len = min(min_len, len(s))

        prefix = ""
        temp_prefix = ""
        all_match_flg = True
        for i in range(min_len):
            base_w = strs[0][i]
            for j in range(len(strs)):
                comp_w = strs[j][i]
                if base_w != comp_w:
                    temp_prefix = ""
                    all_match_flg = False
            if all_match_flg:
                temp_prefix += comp_w
            if len(prefix) < len(temp_prefix):
                prefix = temp_prefix
        
        return prefix
                