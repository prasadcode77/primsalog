def solve_nqueens(n):
    board = []
    def is_safe(r, c):
        for i in range(len(board)):
            if board[i] == c or abs(board[i] - c) == abs(i - r):
                return False
        return True

    def backtrack(r):
        if r == n:
            print(board)
            return
        for c in range(n):
            if is_safe(r, c):
                board.append(c)
                backtrack(r + 1)
                board.pop()

n = int(input("Enter N: "))
solve_nqueens(n)
