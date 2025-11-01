---
layout: post
title: "LC 419: Battleships in a Board"
date: 2025-10-21 17:00:00 -0700
categories: leetcode medium array matrix
permalink: /posts/2025-10-21-medium-419-battleships-in-a-board/
tags: [leetcode, medium, array, matrix, dfs, battleship]
---

# LC 419: Battleships in a Board

**Difficulty:** Medium  
**Category:** Array, Matrix, DFS  
**Companies:** Amazon, Google, Microsoft

## Problem Statement

Given an `m x n` matrix `board` where each cell is either a battleship `'X'` or empty `'.'`, return the number of the battleships on `board`.

Battleships can only be placed horizontally or vertically on `board`. In other words, they can only be made of the shape `1 x k` (1 row, k columns) or `k x 1` (k rows, 1 column), where `k` can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

### Examples

**Example 1:**
```
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
```

**Example 2:**
```
Input: board = [["."]]
Output: 0
```

### Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is either `'.'` or `'X'`

## Solution Approaches

### Approach 1: Count Top-Left Corners (Optimal)

**Key Insight:** Only count the top-left corner of each battleship. A cell is the top-left corner if:
1. It contains `'X'`
2. The cell above it (if exists) is not `'X'`
3. The cell to the left (if exists) is not `'X'`

**Time Complexity:** O(m × n)  
**Space Complexity:** O(1)

```python
class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i > 0 and board[i - 1][j] == 'X':
                        continue
                    if j > 0 and board[i][j - 1] == 'X':
                        continue
                    count += 1
        return count
```

### Approach 2: DFS with Visited Tracking

**Algorithm:**
1. Mark visited battleships to avoid double counting
2. Use DFS to explore each battleship completely
3. Count each battleship only once

**Time Complexity:** O(m × n)  
**Space Complexity:** O(m × n) for visited array

```python
class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and not visited[i][j]:
                    self.dfs(board, visited, i, j)
                    count += 1
        return count
    
    def dfs(self, board: list[list[str]], visited: list[list[bool]], i: int, j: int) -> None:
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or 
            board[i][j] != 'X' or visited[i][j]):
            return
        
        visited[i][j] = True
        
        # Explore in all four directions
        self.dfs(board, visited, i + 1, j)
        self.dfs(board, visited, i - 1, j)
        self.dfs(board, visited, i, j + 1)
        self.dfs(board, visited, i, j - 1)
```

### Approach 3: Union Find

**Algorithm:**
1. Use Union Find to group connected `'X'` cells
2. Count the number of distinct groups

**Time Complexity:** O(m × n × α(m × n)) where α is inverse Ackermann function  
**Space Complexity:** O(m × n)

```python
class Solution:

    def countBattleships(self, board: list[list[str]]) -> int:
        m, n = len(board), len(board[0])
        uf = self.UnionFind(m * n)
        count = 0
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    curr = i * n + j
                    if i > 0 and board[i - 1][j] == 'X':
                        uf.unionSets(curr, (i - 1) * n + j)
                    if j > 0 and board[i][j - 1] == 'X':
                        uf.unionSets(curr, i * n + (j - 1))
        
        roots = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    roots.add(uf.find(i * n + j))
        
        return len(roots)
    
    class UnionFind:
        def __init__(self, n: int):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x: int) -> int:
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def unionSets(self, x: int, y: int) -> None:
            px = self.find(x)
            py = self.find(y)
            if px != py:
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
```

## Algorithm Analysis

### Top-Left Corner Approach (Recommended)

**Why it works:**
- Each battleship has exactly one top-left corner
- By checking only top and left neighbors, we avoid double counting
- No extra space needed

**Key Conditions:**
```python
if(i > 0  board[i - 1][j] == 'X') continue;  // Not top-left
if(j > 0  board[i][j - 1] == 'X') continue;  // Not top-left
```

### Complexity Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Top-Left Corner | O(m×n) | O(1) | Optimal, simple | None |
| DFS | O(m×n) | O(m×n) | Clear logic | Extra space |
| Union Find | O(m×n×α) | O(m×n) | Handles complex shapes | Overkill for this problem |

## Key Insights

1. **Battleship Structure**: Each battleship is a connected component of `'X'` cells
2. **No Adjacent Ships**: Ships are separated by at least one empty cell
3. **Top-Left Corner**: Each battleship has exactly one top-left corner
4. **Single Pass**: Can count ships in one pass without modification

## Edge Cases

1. **Empty Board**: Return 0
2. **Single Cell**: `[["X"]]` → 1 battleship
3. **No Battleships**: `[["."]]` → 0 battleships
4. **Large Battleships**: Vertical or horizontal ships of any length

## Follow-up Questions

- What if battleships could be L-shaped or T-shaped?
- How would you find the size of each battleship?
- What if the board could be modified (mark visited ships)?

## Related Problems

- [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [LC 695: Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [LC 130: Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

## Implementation Notes

1. **Boundary Checks**: Always check array bounds before accessing
2. **Type Casting**: Cast `board.size()` to `int` to avoid comparison warnings
3. **Early Continue**: Use `continue` to skip non-top-left corners
4. **Single Pass**: No need to modify the original board

---

*This problem demonstrates the power of identifying unique characteristics (top-left corners) to solve problems efficiently without extra space.*
