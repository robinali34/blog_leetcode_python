---
layout: post
title: "Algorithm Templates: Backtracking"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates backtracking
permalink: /posts/2025-11-24-leetcode-templates-backtracking/
tags: [leetcode, templates, backtracking, dfs]
---

{% raw %}
Minimal, copy-paste Python for permutations, combinations, subsets, combination sum, grid pathfinding, and constraint satisfaction (N-Queens, Sudoku).

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
# Permutations without duplicates
def permute_backtrack(nums: list[int], cur: list[int], used: list[bool], res: list[list[int]]) -> None:
    if len(cur) == len(nums):
        res.append(cur.copy())
        return
    for i in range(len(nums)):
        if used[i]:
            continue
        used[i] = True
        cur.append(nums[i])
        permute_backtrack(nums, cur, used, res)
        cur.pop()
        used[i] = False
```

### Permutations with duplicates

Avoid duplicates by sorting first, then skipping duplicates at the same level when the previous duplicate hasn't been used.

```python
# Permutations with duplicates (sort first; skip same value at same level if prev unused)
def permute_unique_backtrack(nums: list[int], cur: list[int], used: list[bool], res: list[list[int]]) -> None:
    if len(cur) == len(nums):
        res.append(cur.copy())
        return
    for i in range(len(nums)):
        if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
            continue
        used[i] = True
        cur.append(nums[i])
        permute_unique_backtrack(nums, cur, used, res)
        cur.pop()
        used[i] = False


def permute_unique(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    res: list[list[int]] = []
    permute_unique_backtrack(nums, [], [False] * len(nums), res)
    return res
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 46 | Permutations | [Link](https://leetcode.com/problems/permutations/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-46-permutations/) |
| 47 | Permutations II | [Link](https://leetcode.com/problems/permutations-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-47-permutations-ii/) |

## Combinations (Choose k from n)

Generate all combinations of k elements from n elements. Order doesn't matter, so we use `start` index to avoid duplicates.

```python
# Combinations C(n, k) — choose k numbers from 1..n
def combine_backtrack(start: int, n: int, k: int, cur: list[int], res: list[list[int]]) -> None:
    if len(cur) == k:
        res.append(cur.copy())
        return
    for i in range(start, n + 1):
        cur.append(i)
        combine_backtrack(i + 1, n, k, cur, res)
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
# Subsets without duplicates
def subsets_backtrack(start: int, nums: list[int], cur: list[int], res: list[list[int]]) -> None:
    res.append(cur.copy())
    for i in range(start, len(nums)):
        cur.append(nums[i])
        subsets_backtrack(i + 1, nums, cur, res)
        cur.pop()
```

### Subsets with duplicates

Sort first, then skip duplicates at the same level.

```python
# Subsets with duplicates (sort first, skip duplicates at same level)
def subsets_dup_backtrack(start: int, nums: list[int], cur: list[int], res: list[list[int]]) -> None:
    res.append(cur.copy())
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        cur.append(nums[i])
        subsets_dup_backtrack(i + 1, nums, cur, res)
        cur.pop()


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res: list[list[int]] = []
    subsets_dup_backtrack(0, nums, [], res)
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
# Combination Sum (can reuse same element)
def combination_sum_backtrack(
    start: int, candidates: list[int], target: int, cur: list[int], res: list[list[int]]
) -> None:
    if target == 0:
        res.append(cur.copy())
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        cur.append(candidates[i])
        combination_sum_backtrack(i, candidates, target - candidates[i], cur, res)
        cur.pop()

```

### Combination Sum II (each element used once, duplicates exist)

```python
# Combination Sum II (each element used once, duplicates exist)
def combination_sum2_backtrack(
    start: int, candidates: list[int], target: int, cur: list[int], res: list[list[int]]
) -> None:
    if target == 0:
        res.append(cur.copy())
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        cur.append(candidates[i])
        combination_sum2_backtrack(i + 1, candidates, target - candidates[i], cur, res)
        cur.pop()


def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    res: list[list[int]] = []
    combination_sum2_backtrack(0, candidates, target, [], res)
    return res

```

### Combination Sum III (choose k numbers from 1-9 that sum to n)

```python
# Combination Sum III: choose k numbers from 1-9 that sum to n
def combination_sum3_backtrack(start: int, k: int, n: int, cur: list[int], res: list[list[int]]) -> None:
    if len(cur) == k and n == 0:
        res.append(cur.copy())
        return
    if len(cur) >= k or n < 0:
        return
    for i in range(start, 10):
        cur.append(i)
        combination_sum3_backtrack(i + 1, k, n - i, cur, res)
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
# Word Search: find if word exists in grid
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def word_search_dfs(board: list[list[str]], i: int, j: int, word: str, idx: int) -> bool:
    if idx == len(word):
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    if board[i][j] != word[idx]:
        return False
    temp = board[i][j]
    board[i][j] = "#"
    for di, dj in DIRS:
        if word_search_dfs(board, i + di, j + dj, word, idx + 1):
            board[i][j] = temp
            return True
    board[i][j] = temp
    return False


def word_exist(board: list[list[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if word_search_dfs(board, i, j, word, 0):
                return True
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
# N-Queens: place n queens on n×n board (board is list[list[str]])
def n_queens_is_safe(board: list[list[str]], row: int, col: int, n: int) -> bool:
    for i in range(row):
        if board[i][col] == "Q":
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    return True


def n_queens_backtrack(row: int, n: int, board: list[list[str]], res: list[list[str]]) -> None:
    if row == n:
        res.append(["".join(r) for r in board])
        return
    for col in range(n):
        if n_queens_is_safe(board, row, col, n):
            board[row][col] = "Q"
            n_queens_backtrack(row + 1, n, board, res)
            board[row][col] = "."

```

### Sudoku Solver

```python
# Sudoku Solver (mutates board in place)
def sudoku_valid(board: list[list[str]], row: int, col: int, ch: str) -> bool:
    for i in range(9):
        if board[row][i] == ch:
            return False
        if board[i][col] == ch:
            return False
    br, bc = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[br + i][bc + j] == ch:
                return False
    return True


def solve_sudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                continue
            for d in "123456789":
                if not sudoku_valid(board, i, j, d):
                    continue
                board[i][j] = d
                if solve_sudoku(board):
                    return True
                board[i][j] = "."
            return False
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
# Palindrome Partitioning
def is_pal_sub(s: str, l: int, r: int) -> bool:
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def partition_backtrack(start: int, s: str, cur: list[str], res: list[list[str]]) -> None:
    if start == len(s):
        res.append(cur.copy())
        return
    for end in range(start, len(s)):
        if is_pal_sub(s, start, end):
            cur.append(s[start : end + 1])
            partition_backtrack(end + 1, s, cur, res)
            cur.pop()

```

**Optimization:** Precompute palindrome table to avoid repeated checks.

```python
# Optimized: precompute palindrome table dp[i][j]
def precompute_palindromes(s: str) -> list[list[bool]]:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = True
            elif j == i + 1:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
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
# Generate Parentheses: generate all valid n pairs
def gen_parentheses_backtrack(n: int, open_cnt: int, close_cnt: int, path: list[str], res: list[str]) -> None:
    if len(path) == 2 * n:
        res.append("".join(path))
        return
    if open_cnt < n:
        path.append("(")
        gen_parentheses_backtrack(n, open_cnt + 1, close_cnt, path, res)
        path.pop()
    if close_cnt < open_cnt:
        path.append(")")
        gen_parentheses_backtrack(n, open_cnt, close_cnt + 1, path, res)
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
# Sketch — fill in problem-specific helpers
def backtrack_sketch(state, constraints, current_solution, results):
    if is_complete(current_solution):
        results.append(list(current_solution))
        return
    for candidate in iter_candidates(state):
        if not is_valid_move(candidate, constraints):
            continue
        make_move(candidate, current_solution)
        backtrack_sketch(next_state(state, candidate), constraints, current_solution, results)
        undo_move(candidate, current_solution)

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

