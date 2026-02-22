---
layout: post
title: "Algorithm Templates: Backtracking"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates backtracking
permalink: /posts/2025-11-24-leetcode-templates-backtracking/
tags: [leetcode, templates, backtracking, dfs]
---

{% raw %}
Minimal, copy-paste C++ for permutations, combinations, subsets, combination sum, grid pathfinding, and constraint satisfaction (N-Queens, Sudoku).

## Contents

- [Permutations](#permutations-all-arrangements)
- [Combinations](#combinations-choose-k-from-n)
- [Subsets](#subsets-all-subsets)
- [Combination Sum](#combination-sum-unboundedreuse-elements)
- [Grid Backtracking](#grid-backtracking-word-search-path-finding)
- [Constraint Satisfaction](#constraint-satisfaction-n-queens-sudoku)
- [Palindrome Partitioning](#palindrome-partitioning)
- [General Backtracking Template](#general-backtracking-template)

## Introduction

Backtracking is a systematic way to explore all possible solutions by building candidates incrementally and abandoning ("backtracking") partial candidates that cannot lead to valid solutions. It's essentially a depth-first search with pruning.

**Key Characteristics:**
- Builds solutions incrementally
- Abandons partial solutions that cannot be completed (pruning)
- Uses recursion to explore the solution space
- Restores state after recursive calls (backtracking step)

## Permutations (All Arrangements)

Generate all permutations of distinct elements.

### Permutations without duplicates

```python
// Permutations without duplicates
def backtrack(self, nums, cur, used, res):
    if len(cur) == len(nums):
        res.append(cur)
        return
    for (i = 0 i < (int)len(nums) i += 1):
    if (used[i]) continue
    used[i] = True
    cur.append(nums[i])
    backtrack(nums, cur, used, res)
    cur.pop()
    used[i] = False
```

### Permutations with duplicates

Avoid duplicates by sorting first, then skipping duplicates at the same level when the previous duplicate hasn't been used.

```python
// Permutations with duplicates (avoid duplicates by sorting + skip used duplicates)
def backtrack(self, nums, cur, used, res):
    if len(cur) == len(nums):
        res.append(cur)
        return
    for (i = 0 i < (int)len(nums) i += 1):
    // Skip if already used, or if duplicate and previous duplicate not used
    if (used[i]  or  (i > 0  and  nums[i] == nums[i-1]  and  not used[i-1])) continue
    used[i] = True
    cur.append(nums[i])
    backtrack(nums, cur, used, res)
    cur.pop()
    used[i] = False
// Call with sorted array
def permuteUnique(self, nums):
    nums.sort()
    list[list[int>> res
    list[int> cur
    list[bool> used(len(nums), False)
    backtrack(nums, cur, used, res)
    return res
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 46 | Permutations | [Link](https://leetcode.com/problems/permutations/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-46-permutations/) |
| 47 | Permutations II | [Link](https://leetcode.com/problems/permutations-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-47-permutations-ii/) |

## Combinations (Choose k from n)

Generate all combinations of k elements from n elements. Order doesn't matter, so we use `start` index to avoid duplicates.

```python
// Combinations C(n, k)
def backtrack(self, start, n, k, cur, res):
    if len(cur) == k:
        res.append(cur)
        return
    // Only consider elements from start onwards to avoid duplicates
    for (i = start i <= n i += 1):
    cur.append(i)
    backtrack(i+1, n, k, cur, res)  // Next start is i+1
    cur.pop()
```

**Key insight:** Use `start` parameter to ensure we only consider elements after the current position, preventing duplicate combinations.

| ID | Title | Link | Solution |
|---|---|---|---|
| 77 | Combinations | [Link](https://leetcode.com/problems/combinations/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-77-combinations/) |
| 22 | Generate Parentheses | [Link](https://leetcode.com/problems/generate-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/medium-22-generate-parentheses/) |

## Subsets (All Subsets)

Generate all subsets (power set) of an array. This includes the empty set and the set itself.

### Subsets without duplicates

```python
// Subsets without duplicates
def backtrack(self, start, nums, cur, res):
    res.append(cur)  // Add current subset (including empty set)
    for (i = start i < (int)len(nums) i += 1):
    cur.append(nums[i])
    backtrack(i+1, nums, cur, res)
    cur.pop()
```

### Subsets with duplicates

Sort first, then skip duplicates at the same level.

```python
// Subsets with duplicates (sort first, skip duplicates at same level)
def backtrack(self, start, nums, cur, res):
    res.append(cur)
    for (i = start i < (int)len(nums) i += 1):
    // Skip duplicates at the same level
    if (i > start  and  nums[i] == nums[i-1]) continue
    cur.append(nums[i])
    backtrack(i+1, nums, cur, res)
    cur.pop()
// Call with sorted array
def subsetsWithDup(self, nums):
    nums.sort()
    list[list[int>> res
    list[int> cur
    backtrack(0, nums, cur, res)
    return res
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 78 | Subsets | [Link](https://leetcode.com/problems/subsets/) | - |
| 90 | Subsets II | [Link](https://leetcode.com/problems/subsets-ii/) | - |

## Combination Sum (Unbounded/Reuse Elements)

Find all combinations that sum to target. Elements can be reused or used once depending on the problem.

### Combination Sum (can reuse same element)

```python
// Combination Sum (can reuse same element)
def backtrack(self, start, candidates, target, cur, res):
    if target == 0:
        res.append(cur)
        return
    if (target < 0) return  // Pruning: target exceeded
    for (i = start i < (int)len(candidates) i += 1):
    cur.append(candidates[i])
    // Can reuse: start=i (not i+1)
    backtrack(i, candidates, target - candidates[i], cur, res)
    cur.pop()
```

### Combination Sum II (each element used once, duplicates exist)

```python
// Combination Sum II (each element used once, duplicates exist)
def backtrack(self, start, candidates, target, cur, res):
    if target == 0:
        res.append(cur)
        return
    if (target < 0) return
    for (i = start i < (int)len(candidates) i += 1):
    // Skip duplicates at the same level
    if (i > start  and  candidates[i] == candidates[i-1]) continue
    cur.append(candidates[i])
    // No reuse: start=i+1
    backtrack(i+1, candidates, target - candidates[i], cur, res)
    cur.pop()
// Call with sorted array
def combinationSum2(self, candidates, target):
    candidates.sort()
    list[list[int>> res
    list[int> cur
    backtrack(0, candidates, target, cur, res)
    return res
```

### Combination Sum III (choose k numbers from 1-9 that sum to n)

```python
// Combination Sum III: choose k numbers from 1-9 that sum to n
def backtrack(self, start, k, n, cur, res):
    if len(cur) == k  and  n == 0:
        res.append(cur)
        return
    if (len(cur) >= k  or  n < 0) return
    for (i = start i <= 9 i += 1):
    cur.append(i)
    backtrack(i+1, k, n-i, cur, res)
    cur.pop()
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 39 | Combination Sum | [Link](https://leetcode.com/problems/combination-sum/) | - |
| 40 | Combination Sum II | [Link](https://leetcode.com/problems/combination-sum-ii/) | - |
| 216 | Combination Sum III | [Link](https://leetcode.com/problems/combination-sum-iii/) | - |

## Grid Backtracking (Word Search, Path Finding)

Backtrack on 2D grid with constraints. Mark cells as visited during exploration, then restore them.

### Word Search

```python
// Word Search: find if word exists in grid
def dfs(self, board, i, j, word, idx):
    if (idx == (int)len(word)) return True
    if (i < 0  or  i >= (int)len(board)  or  j < 0  or  j >= (int)board[0].__len__()) return False
    if (board[i][j] != word[idx]) return False
    char temp = board[i][j]
    board[i][j] = '#'  // Mark as visited
    dirs[4][2] = \:\:0,1\, \:0,-1\, \:1,0\, \:-1,0\\
for d in dirs:
    if (dfs(board, i+d[0], j+d[1], word, idx+1)) return True
board[i][j] = temp  // Backtrack: restore original value
return False
def exist(self, board, word):
    for (i = 0 i < (int)len(board) i += 1):
    for (j = 0 j < (int)board[0].__len__() j += 1):
    if (dfs(board, i, j, word, 0)) return True
return False
```

**Key points:**
- Mark cell as visited before recursion
- Restore cell value after recursion (backtracking)
- Check bounds and constraints before recursing

| ID | Title | Link | Solution |
|---|---|---|---|
| 79 | Word Search | [Link](https://leetcode.com/problems/word-search/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/medium-79-word-search/) |
| 212 | Word Search II | [Link](https://leetcode.com/problems/word-search-ii/) | - |
| 351 | Android Unlock Patterns | [Link](https://leetcode.com/problems/android-unlock-patterns/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/02/medium-351-android-unlock-patterns/) |
| 425 | Word Squares | [Link](https://leetcode.com/problems/word-squares/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/hard-425-word-squares/) |
| 489 | Robot Room Cleaner | [Link](https://leetcode.com/problems/robot-room-cleaner/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-hard-489-robot-room-cleaner/) |

## Constraint Satisfaction (N-Queens, Sudoku)

Backtracking with complex constraints. Validate each move before placing.

### N-Queens

```python
// N-Queens: place n queens on n×n board
def backtrack(self, row, n, board, res):
    if row == n:
        res.append(board)
        return
    for (col = 0 col < n col += 1):
    if isValid(board, row, col, n):
        board[row][col] = 'Q'
        backtrack(row+1, n, board, res)
        board[row][col] = '.'  // Backtrack
def isValid(self, board, row, col, n):
    // Check column above
    for i in range(0, row):
    if (board[i][col] == 'Q') return False
    // Check diagonal \ (top-left to bottom-right)
    for (i = row-1, j = col-1 i >= 0  and  j >= 0 i -= 1, j -= 1)
    if (board[i][j] == 'Q') return False
    // Check diagonal / (top-right to bottom-left)
    for (i = row-1, j = col+1 i >= 0  and  j < n i -= 1, j += 1)
    if (board[i][j] == 'Q') return False
    return True
```

### Sudoku Solver

```python
// Sudoku Solver
def solveSudoku(self, board):
    for (i = 0 i < 9 i += 1):
    for (j = 0 j < 9 j += 1):
    if board[i][j] == '.':
        for (char c = '1' c <= '9' c += 1):
        if isValid(board, i, j, c):
            board[i][j] = c
            if (solveSudoku(board)) return True
            board[i][j] = '.'  // Backtrack
    return False  // No valid number found
return True  // All cells filled
def isValid(self, board, row, col, c):
    for (i = 0 i < 9 i += 1):
    // Check row
    if (board[row][i] == c) return False
    // Check column
    if (board[i][col] == c) return False
    // Check 3x3 box
    if (board[3(row/3) + i/3][3(col/3) + i%3] == c) return False
return True
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 51 | N-Queens | [Link](https://leetcode.com/problems/n-queens/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/hard-51-n-queens/) |
| 52 | N-Queens II | [Link](https://leetcode.com/problems/n-queens-ii/) | - |
| 37 | Sudoku Solver | [Link](https://leetcode.com/problems/sudoku-solver/) | - |

## Palindrome Partitioning

Partition string into palindromic substrings. Check if substring is palindrome before partitioning.

```python
// Palindrome Partitioning
def backtrack(self, start, s, cur, res):
    if start == (int)len(s):
        res.append(cur)
        return
    for (end = start end < (int)len(s) end += 1):
    if isPalindrome(s, start, end):
        cur.append(s.substr(start, end-start+1))
        backtrack(end+1, s, cur, res)
        cur.pop()  // Backtrack
def isPalindrome(self, s, l, r):
    while l < r:
        if (s[l += 1] != s[r -= 1]) return False
    return True
```

**Optimization:** Precompute palindrome table to avoid repeated checks.

```python
// Optimized: Precompute palindrome table
def precomputePalindromes(self, s):
    n = len(s)
    list[list[bool>> dp(n, list[bool>(n, False))
    for (i = n-1 i >= 0 i -= 1):
    for (j = i j < n j += 1):
    if (i == j) dp[i][j] = True
elif j == i+1) dp[i][j] = (s[i] == s[j]:
else dp[i][j] = (s[i] == s[j]  and  dp[i+1][j-1])
return dp
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 131 | Palindrome Partitioning | [Link](https://leetcode.com/problems/palindrome-partitioning/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/30/medium-131-palindrome-partitioning/) |
| 132 | Palindrome Partitioning II | [Link](https://leetcode.com/problems/palindrome-partitioning-ii/) | - |
| 5 | Longest Palindromic Substring | [Link](https://leetcode.com/problems/longest-palindromic-substring/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-5-longest-palindromic-substring/) |
| 647 | Palindromic Substrings | [Link](https://leetcode.com/problems/palindromic-substrings/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-647-palindromic-substrings/) |

## Parentheses Generation

Generate all valid parentheses combinations using backtracking.

```python
// Generate Parentheses: generate all valid n pairs
def backtrack(self, n, open, close, path, res):
    if len(path) == 2 * n:
        res.append(path)
        return
    if open < n:
        path.append('(')
        backtrack(n, open + 1, close, path, res)
        path.pop()
    if close < open:
        path.append(')')
        backtrack(n, open, close + 1, path, res)
        path.pop()
```

**Key constraints:**
- `open < n`: Can add opening parenthesis if not all used
- `close < open`: Can add closing parenthesis if there are unmatched openings
- Base case: path length equals `2 * n`

| ID | Title | Link | Solution |
|---|---|---|---|
| 22 | Generate Parentheses | [Link](https://leetcode.com/problems/generate-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/medium-22-generate-parentheses/) |

## General Backtracking Template

```python
def backtrack(self, state, constraints, current_solution, results):
    // Base case: solution is complete
    if isComplete(current_solution):
        results.add(current_solution)
        return
    // Generate candidates
    for (each candidate in candidates):
    // Pruning: skip invalid candidates early
    if isValid(candidate, constraints):
        // Make move: add candidate to solution
        makeMove(candidate, current_solution)
        // Recurse: explore further
        backtrack(updated_state, constraints, current_solution, results)
        // Backtrack: remove candidate to try next option
        undoMove(candidate, current_solution)
```

**Key Points:**
- **Base Case**: When solution is complete, add to results
- **Pruning**: Skip invalid candidates early to reduce search space
- **Make Move**: Add candidate to current solution and update state
- **Recurse**: Explore further with updated state
- **Backtrack**: Remove candidate and restore state to try next option

**Common Optimizations:**
1. **Early pruning**: Check constraints before recursing
2. **Memoization**: Cache results for repeated subproblems (if applicable)
3. **Sorting**: Sort input to handle duplicates efficiently
4. **Precomputation**: Precompute expensive checks (e.g., palindrome table)

**Time Complexity:** Typically exponential O(2^n) or O(n!) depending on problem
**Space Complexity:** O(depth) for recursion stack + O(solution_size) for current solution

## More templates

- **Data structures, Graph, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

