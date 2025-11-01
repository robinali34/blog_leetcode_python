---
layout: post
title: "[Medium] 77. Combinations"
date: 2025-09-29 00:00:00 -0000
categories: python combinations dfs problem-solving
---

# [Medium] 77. Combinations

This is a classic backtracking problem that requires generating all possible combinations of k numbers chosen from the range [1, n]. The key insight is using DFS with backtracking to explore all possible paths while avoiding duplicates.

## Problem Description

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

### Examples

**Example 1:**
```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

**Example 2:**
```
Input: n = 1, k = 1
Output: [[1]]
```

**Example 3:**
```
Input: n = 3, k = 3
Output: [[1,2,3]]
```

### Constraints
- 1 <= n <= 20
- 1 <= k <= n

## Approach

The solution uses backtracking (DFS) with the following strategy:

1. **Base Case**: When the current path has k elements, add it to the result
2. **Early Termination**: If not enough numbers remain to form a valid combination, return early
3. **Recursive Case**: For each number from `first_num` to n, add it to the path and recurse
4. **Backtrack**: Remove the last element before trying the next number
5. **Avoid Duplicates**: Start from `i + 1` in the next recursive call to ensure ascending order

## Solution in Python

**Time Complexity:** O(C(n,k) × k) - We generate C(n,k) combinations, each taking O(k) time  
**Space Complexity:** O(k) - For the recursion stack and current path

```python
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []
        self.dfs(n, k, result, path, 1)
        return result

    def dfs(self, n: int, k: int, result: list[list[int]], path: list[int], first_num: int) -> None:
        if len(path) == k:
            result.append(path[:])
            return
        if len(path) + (n - first_num + 1) < k:
            return
        for i in range(first_num, n + 1):
            path.append(i)
            self.dfs(n, k, result, path, i + 1)
            path.pop()
```

## Step-by-Step Example

Let's trace through the solution with n = 4, k = 2:

**Initial Call:** `dfs(4, 2, rtn, [], 1)`

**Iteration 1:** i = 1
- Add 1 to path: `[1]`
- Recursive call: `dfs(4, 2, rtn, [1], 2)`
  - i = 2: Add 2 → `[1,2]` → Base case hit → Add to result
  - i = 3: Add 3 → `[1,3]` → Base case hit → Add to result  
  - i = 4: Add 4 → `[1,4]` → Base case hit → Add to result
- Remove 1 from path: `[]`

**Iteration 2:** i = 2
- Add 2 to path: `[2]`
- Recursive call: `dfs(4, 2, rtn, [2], 3)`
  - i = 3: Add 3 → `[2,3]` → Base case hit → Add to result
  - i = 4: Add 4 → `[2,4]` → Base case hit → Add to result
- Remove 2 from path: `[]`

**Iteration 3:** i = 3
- Add 3 to path: `[3]`
- Recursive call: `dfs(4, 2, rtn, [3], 4)`
  - i = 4: Add 4 → `[3,4]` → Base case hit → Add to result
- Remove 3 from path: `[]`

**Iteration 4:** i = 4
- Add 4 to path: `[4]`
- Recursive call: `dfs(4, 2, rtn, [4], 5)` → No iterations (i > n)
- Remove 4 from path: `[]`

**Result:** `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`

## Key Insights

1. **Backtracking Pattern**: Add → Recurse → Remove
2. **Avoiding Duplicates**: Use `first_num` parameter to ensure ascending order
3. **Early Termination**: Prune branches where `path.size() + (n - first_num + 1) < k`
4. **Pruning**: Stop when `i > n` or when remaining numbers can't form a valid combination
5. **Base Case**: When path size equals k, we have a valid combination

## Backtracking Template

This problem follows the classic backtracking template:

```python
def backtrack(self, parameters) -> None:
    if base_case:
        # Process result
        return
    
    for choice in choices:
        # Make choice
        make_choice(choice)
        
        # Recurse
        backtrack(updated_parameters)
        
        # Undo choice (backtrack)
        undo_choice(choice)
```

## Alternative Approaches

### Iterative Solution
```python
def combine(self, n: int, k: int) -> list[list[int]]:
    result = []
    combination = list(range(1, k + 1))
    
    while True:
        result.append(combination[:])
        
        i = k - 1
        while i >= 0 and combination[i] == n - k + i + 1:
            i -= 1
        
        if i < 0:
            break
        
        combination[i] += 1
        for j in range(i + 1, k):
            combination[j] = combination[j - 1] + 1
    
    return result
```

### Mathematical Approach (Using Next Permutation)
```python
def combine(self, n: int, k: int) -> list[list[int]]:
    from itertools import combinations
    return list(combinations(range(1, n + 1), k))
```

## Optimization Techniques

### Early Termination
```python
def dfs(self, n: int, k: int, result: list[list[int]], path: list[int], start: int) -> None:
    # Early termination: not enough numbers left
    if len(path) + (n - start + 1) < k:
        return
    
    if len(path) == k:
        result.append(path[:])
        return
    
    for i in range(start, n + 1):
        path.append(i)
        self.dfs(n, k, result, path, i + 1)
        path.pop()
```

## Common Mistakes

1. **Not Backtracking**: Forgetting to remove elements after recursion
2. **Duplicate Combinations**: Not using `first_num` parameter correctly
3. **Index Confusion**: Mixing 0-indexed and 1-indexed ranges
4. **Base Case Errors**: Incorrect termination condition

## Related Problems

- **39. Combination Sum** - Combinations that sum to target
- **40. Combination Sum II** - With duplicates and constraints
- **216. Combination Sum III** - Using digits 1-9 only
- **46. Permutations** - All permutations instead of combinations
- **78. Subsets** - All possible subsets

## Visual Representation

For n = 4, k = 2, the recursion tree looks like:

```
dfs(4,2,[],1)
├── i=1: [1] → dfs(4,2,[1],2)
│   ├── i=2: [1,2] ✓
│   ├── i=3: [1,3] ✓
│   └── i=4: [1,4] ✓
├── i=2: [2] → dfs(4,2,[2],3)
│   ├── i=3: [2,3] ✓
│   └── i=4: [2,4] ✓
├── i=3: [3] → dfs(4,2,[3],4)
│   └── i=4: [3,4] ✓
└── i=4: [4] → dfs(4,2,[4],5) (no iterations)
```

---
