# 🎯 N-Queens Problem using Backtracking (Java)

This project solves the **N-Queens problem** using the **backtracking algorithm** in Java.

---

## 🧠 What is the N-Queens Problem?

The N-Queens problem asks us to place **N queens** on an **N×N chessboard** so that **no two queens attack each other**.  
That means no two queens can be in the same **row**, **column**, or **diagonal**.

---

## ⚙️ How Backtracking Works

Backtracking is like trying all possible ways step by step:

1. Start with the first queen and try to place it in each column of the first row.  
2. If placing it is safe, move to the next queen (next row).  
3. If not safe, try the next column.  
4. If no column works, go back (“backtrack”) to the previous queen and move it to the next position.  
5. Continue until all queens are placed or all options are tried.

This way, we explore all possible placements but backtrack whenever we hit a dead end.

---

## 🧩 Program Explanation

- The program uses an array `x[]` to store the column position of each queen.
- The function `place(k, i)` checks if the queen `k` can be placed in column `i`.
- The function `nQueen(k, n)` tries all possible placements using recursion and prints valid solutions.

---

## 💻 Example Run

**Input:**
4

**Output:**

2 4 1 3
3 1 4 2


Each line shows one valid arrangement of queens on a 4×4 board.

---

## ⏱️ Time & Space Complexity

- **Time:** O(N!) (because of all possible arrangements)
- **Space:** O(N) (for storing positions)

---


