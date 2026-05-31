class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_h = defaultdict(list)
        check_v = defaultdict(list)
        check_box = defaultdict(list)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == ".":
                    continue
                if board[y][x] in check_h[y]:
                    return False
                if board[y][x] in check_v[x]:
                    return False
                if board[y][x] in check_box[tuple([x//3, y//3])]:
                    return False
                check_h[y].append(board[y][x])
                check_v[x].append(board[y][x])
                check_box[tuple([x//3, y//3])].append(board[y][x])

        return True
