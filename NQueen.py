import matplotlib.pyplot as plt
import time

def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def draw_board(board, delay=0.5):
    n = len(board)
    plt.clf()
    fig, ax = plt.subplots()
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(-0.5, n - 0.5)
    ax.set_aspect('equal')
    ax.grid(True)

    for row, col in enumerate(board):
        if col != -1:
            ax.text(col, n - row - 1, '♛', fontsize=20, ha='center', va='center', color='purple')

    plt.pause(delay)

def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            draw_board(board, delay=1.0)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                draw_board(board)
                backtrack(row + 1)
                board[row] = -1
                draw_board(board)

    plt.ion()
    backtrack(0)
    plt.ioff()
    print(f"Total solutions found: {len(solutions)}")
    return solutions

# Run the solver
if _name_ == "_main_":
    N = 4  # Change this to any N ≥ 4
    solve_n_queens(N)