class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs:
                # closing bracket: must match the top of the stack
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                # opening bracket
                stack.append(ch)

        # valid only if every opening bracket was closed
        return not stack