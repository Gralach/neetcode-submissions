class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal, vertical = 9 , 9
        check_x, check_y, check_box = defaultdict(list), defaultdict(list), defaultdict(list)
        for x in range(horizontal):
            for y in range(vertical):
                if board[x][y] == ".":
                    continue
                if (board[x][y] in check_x[x]) or (board[x][y] in check_y[y]) or (board[x][y] in check_box[tuple([x//3,y//3])]):
                    return False
                else:
                    check_x[x].append(board[x][y])
                    check_y[y].append(board[x][y])
                    check_box[tuple([x//3,y//3])].append(board[x][y])
        return True