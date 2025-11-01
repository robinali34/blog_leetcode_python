---
layout: post
title: "[Medium] 54. Spiral Matrix"
categories: python spiral-matrix problem-solving
---

# [Medium] 54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

## Examples

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

## Approach

There are two main approaches to solve this problem:

1. **Boundary Tracking**: Use four boundaries (top, bottom, left, right) and traverse in spiral order
2. **Direction Simulation**: Use direction vectors and mark visited cells to simulate spiral movement

## Solution 1: Boundary Tracking Approach

```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rows, cols = len(matrix), len(matrix[0])
        up, left = 0, 0
        right, down = cols - 1, rows - 1
        
        while len(result) < rows * cols:
            # Traverse right along top row
            for col in range(left, right + 1):
                result.append(matrix[up][col])
            
            # Traverse down along right column
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])
            
            # Traverse left along bottom row (if not same as top)
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])
            
            # Traverse up along left column (if not same as right)
            if left != right:
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])
            
            # Move boundaries inward
            left += 1
            right -= 1
            up += 1
            down -= 1
        return result
```

**Time Complexity:** O(m × n) - Visit each cell exactly once
**Space Complexity:** O(1) - Only using variables for boundaries

## Solution 2: Direction Simulation Approach

```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        VISITED = 101
        rows, cols = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        dir_idx = 0
        result = []
        row, col = 0, 0
        
        for _ in range(rows * cols):
            result.append(matrix[row][col])
            matrix[row][col] = VISITED  # Mark as visited
            
            # Calculate next position
            nextRow = row + dirs[dir_idx][0]
            nextCol = col + dirs[dir_idx][1]
            
            # Check if next position is valid and not visited
            if (0 <= nextRow < rows and 0 <= nextCol < cols and 
                matrix[nextRow][nextCol] != VISITED):
                row, col = nextRow, nextCol
            else:
                # Change direction and move
                dir_idx = (dir_idx + 1) % 4
                row += dirs[dir_idx][0]
                col += dirs[dir_idx][1]
        return result
```

**Time Complexity:** O(m × n) - Visit each cell exactly once
**Space Complexity:** O(1) - Only using variables for direction and position

## Step-by-Step Example (Solution 1)

For matrix = [[1,2,3],[4,5,6],[7,8,9]]:

1. **Initial boundaries:** up=0, down=2, left=0, right=2
2. **Right traversal:** [1,2,3] → rtn = [1,2,3]
3. **Down traversal:** [6,9] → rtn = [1,2,3,6,9]
4. **Left traversal:** [8,7] → rtn = [1,2,3,6,9,8,7]
5. **Up traversal:** [4] → rtn = [1,2,3,6,9,8,7,4]
6. **Update boundaries:** up=1, down=1, left=1, right=1
7. **Right traversal:** [5] → rtn = [1,2,3,6,9,8,7,4,5]

Final result: [1,2,3,6,9,8,7,4,5]

## Key Insights

1. **Boundary Management**: Track four boundaries and move them inward after each complete spiral
2. **Edge Cases**: Handle single row/column matrices with conditional checks
3. **Direction Changes**: Use direction vectors to simulate spiral movement
4. **Visited Marking**: Mark cells as visited to avoid revisiting them

## Solution Comparison

- **Boundary Tracking**: More intuitive, doesn't modify input matrix, cleaner logic
- **Direction Simulation**: More general approach, can be extended to other spiral problems

## Common Mistakes

1. **Off-by-one errors** in boundary conditions
2. **Not handling single row/column** cases properly
3. **Incorrect boundary updates** after each spiral
4. **Missing edge cases** for 1x1 matrices

## Related Problems

- [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)
- [885. Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/)
- [2326. Spiral Matrix IV](https://leetcode.com/problems/spiral-matrix-iv/)
