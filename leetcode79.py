def exist(board, word):
    def backtrack(i, j, k):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        
        temp, board[i][j] = board[i][j], '/'
        found = (backtrack(i + 1, j, k + 1) or
                 backtrack(i - 1, j, k + 1) or
                 backtrack(i, j + 1, k + 1) or
                 backtrack(i, j - 1, k + 1))
        board[i][j] = temp
        return found
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    return False

# test cases
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
print(exist(board1, word1))  # Output: True

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
print(exist(board2, word2))  # Output: True

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"
print(exist(board3, word3))  # Output: False
