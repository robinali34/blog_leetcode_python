---
layout: post
title: "[Medium] 794. Valid Tic-Tac-Toe State"
date: 2025-09-24 17:00:00 -0000
categories: python tic-tac-toe game-validation problem-solving
---

# [Medium] 794. Valid Tic-Tac-Toe State

This is a simulation problem that requires understanding the rules of Tic-Tac-Toe and validating whether a given board state is possible. The key insight is checking the count of X's and O's, and ensuring that winning conditions are valid.

## Problem Description

Given a Tic-Tac-Toe board as an array of strings, return whether this board state is valid.

A Tic-Tac-Toe board is valid if:
1. The number of X's and O's follows the game rules
2. Only one player can win
3. If X wins, there should be exactly one more X than O
4. If O wins, there should be equal number of X's and O's

### Examples

**Example 1:**
```
Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
```

**Example 2:**
```
Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.
```

**Example 3:**
```
Input: board = ["XXX","   ","OOO"]
Output: false
Explanation: Both players win at the same time.
```

### Constraints
- board.length == 3
- board[i].length == 3
- board[i][j] is either 'X', 'O', or ' '

## Approach

The solution involves checking several conditions:

1. **Count Validation**: Count X's and O's - X should have equal or one more count than O
2. **Win Detection**: Check if either player has won (rows, columns, diagonals)
3. **Win Validation**: 
   - If X wins, O should have exactly one less count than X
   - If O wins, X and O should have equal counts
   - Both players cannot win simultaneously

## Solution in Python

**Time Complexity:** O(1) - Constant time since board is always 3x3  
**Space Complexity:** O(1) - Only using constant extra space

```python
class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        x_cnt = sum(row.count('X') for row in board)
        o_cnt = sum(row.count('O') for row in board)
        if x_cnt not in (o_cnt, o_cnt + 1):
            return False
        x_win = self.win(board, 'X')
        o_win = self.win(board, 'O')
        if x_win and o_win:
            return False
        if x_win and x_cnt != o_cnt + 1:
            return False
        if o_win and x_cnt != o_cnt:
            return False
        return True

    def win(self, board: list[str], p: str) -> bool:
        n = 3
        for i in range(n):
            if all(board[i][j] == p for j in range(n)):
                return True
            if all(board[j][i] == p for j in range(n)):
                return True
        if all(board[i][i] == p for i in range(n)):
            return True
        if all(board[i][n - 1 - i] == p for i in range(n)):
            return True
        return False
```

## Step-by-Step Example

Let's trace through the solution with board = `["XOX"," X ","OOO"]`:

**Step 1:** Count X's and O's
- X count: 3 (positions: (0,0), (0,2), (1,1))
- O count: 3 (positions: (0,1), (2,0), (2,1), (2,2))
- Check: `x_cnt != o_cnt + 1 && x_cnt != o_cnt` → `3 != 4 && 3 != 3` → `true && false` → `false` ✓

**Step 2:** Check for wins
- X wins: Check rows, columns, diagonals → No win for X
- O wins: Row 2 has all O's → O wins ✓

**Step 3:** Validate win conditions
- O wins and `o_cnt != x_cnt` → `3 != 3` → `false` ✓
- Both X and O don't win simultaneously ✓

**Result:** Valid board state

## Key Insights

1. **Turn Order**: X always goes first, so X should have equal or one more count than O
2. **Win Detection**: Check all rows, columns, and both diagonals
3. **Mutual Exclusivity**: Only one player can win in a valid game
4. **Count Validation**: Winning player must have the correct count based on game rules

## Common Mistakes

- Not checking if both players win simultaneously
- Incorrect count validation (allowing O to have more pieces than X)
- Missing diagonal win conditions
- Not handling edge cases like empty boards

---
