class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # need to check 3 rules
        # small 3 x 3 boxes
        check_small = defaultdict(list)
        # horizontal sudoku
        check_horizontal = defaultdict(list)
        # vertical_sudoku
        check_vertical = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                # small 3 x 3 boxes
                if board[i][j] == ".":
                    continue
                if board[i][j] in (check_small[i//3, j//3] 
                or check_vertical[i] 
                or check_horizontal[j]):
                    return False
                else:
                    check_small[i//3,j//3].append(board[i][j])
                    check_vertical[i].append(board[i][j])
                    check_horizontal[j].append(board[i][j])
        return True

        
        