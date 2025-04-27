class Solution:
    def interpret(self, command: str) -> str:
        lst = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                lst.append("G")
                i += 1
            elif i + 1 < len(command) and command[i] == "(" and command[i+1] == ")":
                lst.append("o")
                i += 2
            else:
                lst.append("al")
                i += 4
        return ''.join(lst)
