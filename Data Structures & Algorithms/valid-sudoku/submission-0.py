class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(list)
        vertical = defaultdict(list)
        horizontal = defaultdict(list)

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if (board[x][y] in boxes[x//3, y//3] or 
                board[x][y] in vertical[y] or
                board[x][y] in horizontal[x]):
                    return False
                boxes[x//3,y//3].append(board[x][y])
                horizontal[x].append(board[x][y])
                vertical[y].append(board[x][y])
        return True