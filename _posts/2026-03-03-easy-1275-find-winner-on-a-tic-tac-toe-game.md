---
layout: post
title: "1275. Find Winner on a Tic Tac Toe Game"
date: 2026-03-03 00:00:00 -0700
categories: [leetcode, easy, array, simulation]
tags: [leetcode, easy, array, simulation, game]
permalink: /2026/03/03/easy-1275-find-winner-on-a-tic-tac-toe-game/
---

# 1275. Find Winner on a Tic Tac Toe Game

## Problem Statement

Tic-tac-toe is played by two players **A** and **B** on a **3 x 3** grid. The rules are:

- Players take turns placing a character into an empty cell.
- The first player **A** always places `'X'`, and the second player **B** always places `'O'`.
- The game ends when there are **three of the same** character filling any row, column, or diagonal.
- The game also ends if all cells are filled without a winner.

You are given a 2D integer array `moves` where `moves[i] = [row_i, col_i]` indicates that the \(i\)-th move was played on the cell `grid[row_i][col_i]`. Return the winner of the game:

- **"A"** if A wins
- **"B"** if B wins
- **"Draw"** if the game ends in a draw (no winner and board full)
- **"Pending"** if the game is still in progress

Assume that `moves` is **valid** (no repeated cells, no moves after the game ends).

## Examples

**Example 1:**

```python
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins (diagonal: 0,0 -> 1,1 -> 2,2).
```

**Example 2:**

```python
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins (column 0).
```

**Example 3:**

```python
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: Board is full, no winner.
```

## Constraints

- `1 <= moves.length <= 9`
- `moves[i].length == 2`
- `0 <= row_i, col_i <= 2`
- All `moves` are unique and no repeated moves
- Moves follow the rules of tic-tac-toe

## Clarification Questions

1. **Move order**: Odd-indexed moves (0, 2, 4, …) are A, even-indexed (1, 3, 5, …) are B?  
   **Assumption**: Yes — move index `i`: A if `i % 2 == 0`, B if `i % 2 == 1`.
2. **Win detection**: Only check after each move, and return as soon as someone wins?  
   **Assumption**: Yes — we can check after every move.
3. **Valid input**: No invalid or duplicate moves?  
   **Assumption**: Yes — input is valid per problem.
4. **Return**: One of `"A"`, `"B"`, `"Draw"`, `"Pending"`?  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: Simulate the grid (5 min)**  
Build a 3×3 grid, fill it with moves, then after each move check all rows, columns, and diagonals for three X’s or three O’s. Straightforward but requires maintaining a full board and multiple checks.

**Step 2: Track row/col/diag sums (7 min)**  
We don’t need the full grid. For each row, column, main diagonal, and anti-diagonal, maintain a **score**:
- Player A adds +1, Player B adds -1.
- If any line sums to +3, A wins; if -3, B wins.

So we only need:
- `rows[0..2]`, `cols[0..2]`
- `diag` (row == col)
- `antiDiag` (row == 2 - col)

**Step 3: Check after each move (8 min)**  
After updating the scores for the current move, check if any of the eight lines equals `3` or `-3`. If so, return the winner. If all moves are played and no one won, return `"Draw"`; otherwise `"Pending"`.

## Solution Approach

Use four groups of counters:

1. **rows[r]** — sum for row `r` (+1 for A, -1 for B).
2. **cols[c]** — sum for column `c`.
3. **diag** — sum for cells where `row == col`.
4. **antiDiag** — sum for cells where `row == SIZE - 1 - col`.

For each move:
- Determine `player = 1` (A) or `-1` (B) from move index.
- Update `rows[row]`, `cols[col]`, and optionally `diag` and `antiDiag`.
- If any of these equals `3` or `-3`, return `"A"` or `"B"`.
- After processing all moves, return `"Draw"` if there were 9 moves, else `"Pending"`.

### Key Insights

1. **No grid needed** — Only the sum per row, column, and two diagonals matters.
2. **One pass** — Process moves in order and check for a win after each update.
3. **Main vs anti-diagonal** — Main: `row == col`. Anti: `row + col == SIZE - 1` (or `row == SIZE - 1 - col`).
4. **Draw vs Pending** — Draw only when `len(moves) == 9` and no winner; otherwise Pending.

## Python Solution

```python
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        SIZE = 3
        rows = [0] * SIZE
        cols = [0] * SIZE
        diag = 0
        antiDiag = 0

        for i, move in enumerate(moves):
            row, col = move[0], move[1]
            player = 1 if i % 2 == 0 else -1

            rows[row] += player
            cols[col] += player
            if row == col:
                diag += player
            if row == SIZE - 1 - col:
                antiDiag += player

            if (
                rows[row] == SIZE
                or cols[col] == SIZE
                or diag == SIZE
                or antiDiag == SIZE
            ):
                return "A"
            if (
                rows[row] == -SIZE
                or cols[col] == -SIZE
                or diag == -SIZE
                or antiDiag == -SIZE
            ):
                return "B"

        return "Draw" if len(moves) == SIZE * SIZE else "Pending"
```

## Algorithm Explanation

- **Player encoding**: A = +1, B = -1, so three in a row sum to 3 or -3.
- **Updates**: For each move `(row, col)`, add `player` to `rows[row]`, `cols[col]`, and to `diag` / `antiDiag` when the cell lies on those diagonals.
- **Win check**: Right after updating, if any of the eight values is 3 or -3, return the corresponding winner.
- **Termination**: If we finish all moves without a win, return `"Draw"` when there are 9 moves (full board), otherwise `"Pending"`.

## Complexity Analysis

- **Time Complexity**: \(O(m)\), where \(m\) is the number of moves (at most 9).
- **Space Complexity**: \(O(1)\) — fixed number of counters (3 + 3 + 1 + 1).

## Edge Cases

- A wins on the last move (e.g. diagonal).
- B wins on the last move.
- Draw: exactly 9 moves, no line sums to ±3.
- Pending: fewer than 9 moves and no winner yet.
- Win on a row, column, main diagonal, or anti-diagonal — all handled by the same check.

## Common Mistakes

- Forgetting to update or check the anti-diagonal (`row == SIZE - 1 - col`).
- Using the wrong player sign for the move index (e.g. swapping A and B).
- Returning `"Draw"` when moves length is 9 but a winner was already found earlier (our loop returns as soon as a win is detected, so this is avoided).
- Checking only the current row/col/diag instead of all lines that could have changed (here only the current row, col, and possibly the two diagonals change, so the check is correct).

## Related Problems

- [LC 1344: Angle Between Hands of a Clock](/2026/03/03/medium-1344-angle-between-hands-of-a-clock/) — Another simple simulation / arithmetic problem.
- [LC 348: Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) — Same win logic in a design problem (n×n board).
