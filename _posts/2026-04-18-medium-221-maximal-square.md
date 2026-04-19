---
layout: post
title: "[Medium] 221. Maximal Square"
date: 2026-04-18 00:00:00 -0700
categories: [leetcode, medium, array, matrix, dynamic-programming]
permalink: /2026/04/18/medium-221-maximal-square/
tags: [leetcode, medium, matrix, dynamic-programming, 2d-dp]
---

# [Medium] 221. Maximal Square

Given an `m x n` binary `matrix` filled with `'0'` and `'1'`, find the largest square containing only `'1'` and return its **area**.

## How the DP Table Is Built

Define:

`dp[i][j]` = side length of the **largest** square of `'1'`s whose **bottom-right corner** is cell `(i, j)`.

### Transition

If `matrix[i][j] == '1'`:

```text
dp[i][j] = 1 + min(
    dp[i - 1][j],      # top
    dp[i][j - 1],      # left
    dp[i - 1][j - 1]   # top-left
)
```

If `matrix[i][j] == '0'`:

`dp[i][j] = 0`

The answer is `max(dp[i][j]) ** 2` (area = side²).

### Example Walkthrough

Matrix:

```text
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

`dp` (side lengths):

```text
1 0 1 0 0
1 0 1 1 1
1 1 1 2 2
1 0 0 1 0
```

Largest side = **2** → area = **4**.

## Solution (Python)

```python
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(
                            dp[i - 1][j],
                            dp[i][j - 1],
                            dp[i - 1][j - 1],
                        )
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side
```

## Solution (C++)

```cpp
#include <algorithm>
#include <vector>

class Solution {
 public:
  int maximalSquare(std::vector<std::vector<char>>& matrix) {
    if (matrix.empty()) {
      return 0;
    }
    const int rows = static_cast<int>(matrix.size());
    const int cols = static_cast<int>(matrix[0].size());
    std::vector<std::vector<int>> dp(rows, std::vector<int>(cols, 0));
    int max_side = 0;

    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        if (matrix[i][j] == '1') {
          if (i == 0 || j == 0) {
            dp[i][j] = 1;
          } else {
            dp[i][j] = 1 + std::min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
          }
          max_side = std::max(max_side, dp[i][j]);
        }
      }
    }
    return max_side * max_side;
  }
};
```

## Complexity

- **Time:** `O(m * n)`
- **Space:** `O(m * n)` for the `dp` table (can be optimized to `O(n)` with one row)
