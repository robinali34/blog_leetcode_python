---
layout: post
title: "[Medium] 498. Diagonal Traverse"
date: 2026-01-20 00:00:00 -0700
categories: [leetcode, medium, array, matrix, simulation]
permalink: /2026/01/20/medium-498-diagonal-traverse/
tags: [leetcode, medium, array, matrix, simulation]
---

Given an `m x n` matrix `mat`, return an array of all the elements of the matrix in a **diagonal order**.

## Examples

**Example 1:**
```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

**Example 2:**
```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `-10^5 <= mat[i][j] <= 10^5`

## Thinking Process

Given an `m x n` matrix `mat`, return an array of all the elements of the matrix in a **diagonal order**.

- Treat the grid as a graph with 4- or 8-directional neighbors.
- Row-major vs column-major traversal affects cache and logic.
- Boundary checks on every neighbor expansion.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Grid traversal</text>

  <rect x="50" y="40" width="28" height="28" fill="#D4D8E0" stroke="#8B8680"/><rect x="78" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="106" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="50" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="78" y="68" width="28" height="28" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="106" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="110" y="115" text-anchor="middle" font-size="11" fill="#6B6560">BFS/DFS flood from each cell</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Row/column traversal** *(this problem)* | O(nm) | O(1) | Simulation, spiral |
| BFS/DFS on grid | O(nm) | O(nm) | Islands, shortest path |
| Matrix as graph | O(nm) | O(nm) | 4/8-directional neighbors |
| Transpose / rotate | O(nm) | O(1) | In-place rotation tricks |

## Solution
{% raw %}
```python
class Solution:
    def findDiagonalOrder(self, mat):
        M, N = len(mat), len(mat[0])
        TOTAL = M * N
        
        row, col, dirIdx = 0, 0, 0
        rtn = [0] * TOTAL
        
        DIRS = [(-1, 1), (1, -1)]
        
        for i in range(TOTAL):
            rtn[i] = mat[row][col]
            
            nextRow = row + DIRS[dirIdx][0]
            nextCol = col + DIRS[dirIdx][1]
            
            if nextRow < 0 or nextRow >= M or nextCol < 0 or nextCol >= N:
                dirIdx = 1 - dirIdx
                
                if dirIdx == 0:
                    if row == M - 1:
                        col += 1
                    else:
                        row += 1
                else:
                    if col == N - 1:
                        row += 1
                    else:
                        col += 1
            else:
                row = nextRow
                col = nextCol
        
        return rtn
```
{% endraw %}

### Solution Explanation

**Approach:** Row/column traversal (this problem)

**Key idea:** Given an `m x n` matrix `mat`, return an array of all the elements of the matrix in a **diagonal order**.

**How the code works:**
- Treat the grid as a graph with 4- or 8-directional neighbors.
- Row-major vs column-major traversal affects cache and logic.
- Boundary checks on every neighbor expansion.

**Walkthrough** — input `mat = [[1,2,3],[4,5,6],[7,8,9]]`, expected output `[1,2,4,7,5,3,6,8,9]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

- **Time Complexity:** O(m × n) — visit each cell exactly once
- **Space Complexity:** O(1) extra space (excluding the output array)
## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [LC 54. Spiral Matrix](https://www.leetcode.com/problems/spiral-matrix/)
- [LC 1424. Diagonal Traverse II](https://www.leetcode.com/problems/diagonal-traverse-ii/)

## Key Takeaways

- **Pattern:** Row/column traversal (this problem)
- Treat the grid as a graph with 4- or 8-directional neighbors.
- Row-major vs column-major traversal affects cache and logic.

## References

- [LC 498: Diagonal Traverse on LeetCode](https://www.leetcode.com/problems/diagonal-traverse/)
- [LeetCode Discuss — LC 498: Diagonal Traverse](https://www.leetcode.com/problems/diagonal-traverse/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/diagonal-traverse/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/posts/2025-11-24-leetcode-templates-array-matrix/)
