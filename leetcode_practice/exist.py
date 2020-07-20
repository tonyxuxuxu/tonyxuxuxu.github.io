class Solution:
    def exist(self, board, word):
        row = len(board[0])
        col = len(board)
        def dfs(board,word, i, j):
            if len(word) == 0:
                return True
            if i < 0 or i >= row or j <0 or j>= col or word[0] != board[j][i]:
                return False
            
            temp = board[j][i]
            board[j][i] = '#'

            res = dfs(board, word[1:], i+1, j) or dfs(board, word[1:], i, j+1) \
                    or dfs(board, word[1:], i-1, j) or dfs(board, word[1:], i, j-1)
            
            board[j][i] = temp
            return res
