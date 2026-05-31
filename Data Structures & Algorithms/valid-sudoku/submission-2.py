class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_horizontal = defaultdict(list)
        check_vertical = defaultdict(list)
        check_box = defaultdict(list)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                elif ((board[i][j] in check_horizontal[i]) or (board[i][j] in check_vertical[j])or (board[i][j] in check_box[(i//3, j//3)])):
                    return False
                check_horizontal[i].append(board[i][j])
                check_vertical[j].append(board[i][j])
                check_box[(i//3,j//3)].append(board[i][j])
        return True
                    