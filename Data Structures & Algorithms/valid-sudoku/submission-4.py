class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_h = defaultdict(list)
        check_v = defaultdict(list)
        check_box = defaultdict(list)
        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if board[x][y] in check_h[x]:
                    return False
                if board[x][y] in check_v[y]:
                    return False
                if board[x][y] in check_box[tuple([x//3, y//3])]:
                    return False
                check_h[x].append(board[x][y])
                check_v[y].append(board[x][y])
                check_box[tuple([x//3, y//3])].append(board[x][y])
        return True