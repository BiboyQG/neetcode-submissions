class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        open_left = []
        map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        for bracket in s:
            if bracket in map.keys():
                open_left.append(bracket)
            elif open_left and map[open_left[-1]] == bracket:
                open_left.pop()
            else:
                return False
        if open_left: return False
        return True