# 制約
# 文字列の長さは15まで

## 復習する

class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntDict = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000
        )

        ans = 0
        num_list = [romanToIntDict[ss] for _, ss in enumerate(list(s))]
        comp_list = []

        now = num_list[0]
        cnt = 1
        for i in range(1, len(num_list)):
            if now == num_list[i]:
                cnt += 1
            else:
                comp_list.append([now, cnt])
                now = num_list[i]
                cnt = 1
        comp_list.append([now, cnt])
        
        ans = 0
        for i in range(1, len(comp_list)):
            add_num = comp_list[i - 1][0] * comp_list[i - 1][1]
            if comp_list[i - 1][0] > comp_list[i][0]:
                ans += add_num
            else:
                ans -= add_num
        ans += comp_list[-1][0] * comp_list[-1][1]
        return ans
