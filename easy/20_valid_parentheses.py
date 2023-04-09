
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        comb = {"(": ")", "{": "}", "[": "]"}
        for i in range(len(s)):
            if s[i] in {"{", "(", "["}:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if comb.get(left) != s[i]:
                    return False
        return len(stack) == 0